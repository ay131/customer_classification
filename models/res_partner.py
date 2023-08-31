from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    classification_id = fields.Many2one('customer.classification', string='Classification', tracking=True)
