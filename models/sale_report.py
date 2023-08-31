from odoo import models, fields, api

class SaleReport(models.Model):
    _inherit = 'sale.report'

    classification_id = fields.Many2one('customer.classification', string='Classification', readonly=True)

    def _select_additional_fields(self, fields):
        fields['classification_id'] = ", s.classification_id"
        return super()._select_additional_fields(fields)
