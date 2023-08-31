# -*- coding: utf-8 -*-

from odoo import models, fields, api
import uuid


class ResUsers(models.Model):
    _inherit = 'res.users'

    api_key = fields.Char(string='API Key', readonly=False)
    def _generate_token(self):
        return uuid.uuid4().hex

    def generate_api_key(self):
        self.api_key = self._generate_token()
        return True
