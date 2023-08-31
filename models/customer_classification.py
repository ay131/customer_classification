from odoo import models, fields, api


class CustomerClassification(models.Model):
    _name = 'customer.classification'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _description = 'Customer Classification'
    _rec_name = 'title'

    title = fields.Char(string='Title', required=True, tracking=True)
    score = fields.Integer(string='Score', required=True, tracking=True)

