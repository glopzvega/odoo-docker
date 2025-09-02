from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    x_demo_field = fields.Char(string='Extra Field Custom')
