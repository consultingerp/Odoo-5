# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    label_attr_1 = fields.Char(
        string="Label attribute 1",
        required=False,
    )
    label_attr_2 = fields.Char(
        string="Label attribute 2",
        required=False,
    )
    label_attr_3 = fields.Char(
        string="Label attribute 3",
        required=False,
    )
    label_attr_4 = fields.Char(
        string="Label attribute 4",
        required=False,
    )
    label_attr_5 = fields.Char(
        string="Label attribute 5",
        required=False,
    )
