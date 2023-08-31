# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, Response, route
from odoo.exceptions import AccessDenied


class CustomerClassificationApis(http.Controller):
    @route('/api/authenticate', type='json', auth='public', methods=['GET', 'POST'], cors='*', csrf=False)
    def customer_classification_login(self, **kw):
        if not kw.get('email') or not kw.get('password'):
            Response.status = '400'
            return {'error': 'Email and password are required'}
        try:
            uid = request.session.authenticate(request.db, kw.get('email'), kw.get('password'))
            if uid:
                user = request.env['res.users'].sudo().browse(uid)
                user.generate_api_key()
                Response.status = '200'
                return {'api_key': user.api_key}
            else:
                Response.status = '401'
                return {'error': 'Invalid credentials'}
        except AccessDenied as e:
            try:
                user_exist = request.env['res.users'].sudo().search([('login', '=', kw.get('email'))])
                if user_exist:
                    Response.status = '401'
                    return {'error': 'Invalid Password'}
                else:
                    Response.status = '401'
                    return {'error': 'User not found'}
            except Exception as e:
                Response.status = '500'
                return {'error': e}
            Response.status = '500'
            return {'error': e}

    @route('/api/customer_classification/list', type='json', auth='public', methods=['POST', 'GET'], cors='*',
           csrf=False)
    def customer_classification_list(self, **kw):
        auth = request.httprequest.headers.get('Authorization')
        try:
            if auth:
                user = request.env['res.users'].sudo().search([('api_key', '=', auth)])
                if user:
                    classifications_list = []
                    classifications = request.env['customer.classification'].sudo().search_read([])
                    for classification in classifications:
                        classifications_list.append({
                            "id": classification['id'],
                            "title": classification['title'],
                            "score": classification['score'],
                        })
                    Response.status = '200'
                    return {'classifications': classifications_list}
                else:
                    Response.status = '401'
                    return {'error': 'Invalid credentials'}
            else:
                Response.status = '401'
                return {'error': 'Invalid credentials'}
        except Exception as e:
            Response.status = '500'
            return {'error': e}
