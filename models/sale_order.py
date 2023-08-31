from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    classification_id = fields.Many2one('customer.classification', string='Classification',compute='_compute_classification_id', store=True)

    @api.model
    def create(self, vals):
        res = super(SaleOrder, self).create(vals)
        if res.partner_id.classification_id.score > 70:
            for line in res.order_line:
                line.discount = 1.0
        return res

    @api.depends('partner_id', 'partner_id.classification_id', 'partner_id.classification_id.score'
        ,'partner_id.classification_id.title')
    def _compute_classification_id(self):
        for rec in self:
            rec.classification_id = rec.partner_id.classification_id