# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    tag_id = fields.Many2one(comodel_name="stock.product.tag", string="Tag")


class StockProductTag(models.Model):
    _name = 'stock.product.tag'
    _description = 'Stock Product Tag'

    name = fields.Char(required=True)

    label_width = fields.Integer(string="Label Width (MM)",
                                 required=True,
                                 default=57)
    label_height = fields.Integer(string="Label Height (MM)",
                                  required=True,
                                  default=35)
    template = fields.Selection(
        selection=[('product_custom_label.report_product_label',
                    'Label 57x35mm (A4: 21 pcs on sheet, 3x7)')],
        string='Label template',
        default='product_custom_label.report_product_label',
    )

    tags_line_ids = fields.One2many(
        comodel_name="stock.product.tag.line",
        inverse_name="tag_id",
        string="Tags Lines",
    )

    #     Display fields
    is_product_name = fields.Boolean(string="Product Name", default=True)
    is_product_price = fields.Boolean(string="Product Price", default=True)
    is_product_attr = fields.Boolean(string="Product Attributes", default=True)
    is_product_barcode = fields.Boolean(string="Product Barcode", default=True)

    is_label_attr_1 = fields.Boolean(string="Label Attr. 1", default=False)
    is_label_attr_2 = fields.Boolean(string="Label Attr. 2", default=False)
    is_label_attr_3 = fields.Boolean(string="Label Attr. 3", default=False)
    is_label_attr_4 = fields.Boolean(string="Label Attr. 4", default=False)
    is_label_attr_5 = fields.Boolean(string="Label Attr. 5", default=False)

    fz_product_name = fields.Integer(string="Product Name Font Size",
                                     default=16)
    fz_product_price = fields.Integer(string="Product Price Font Size",
                                      default=16)
    fz_product_attr = fields.Integer(string="Product Attributes Font Size",
                                     default=16)
    fz_product_barcode = fields.Integer(string="Product Barcode Font Size",
                                        default=16)

    color_label_attr_1 = fields.Char(string="Color Label Attr. 1",
                                     default="#00000")
    color_label_attr_2 = fields.Char(string="Color Label Attr. 2",
                                     default="#00000")
    color_label_attr_3 = fields.Char(string="Color Label Attr. 3",
                                     default="#00000")
    color_label_attr_4 = fields.Char(string="Color Label Attr. 4",
                                     default="#00000")
    color_label_attr_5 = fields.Char(string="Color Label Attr. 5",
                                     default="#00000")


class StockProductTagLine(models.Model):
    _name = 'stock.product.tag.line'
    _description = 'Stock Product Tag Line'

    tag_id = fields.Many2one(
        comodel_name="stock.product.tag",
        string="Tag",
    )

    sequence = fields.Integer(
        'Sequence',
        default=1,
        help='Gives the sequence order when displaying a product list')

    font_size = fields.Integer(string="Font Size", default=16)
    font_color = fields.Char(string="Font Color",
                             help="Choose your color",
                             default="#000000")
    product_attribute = fields.Many2one(comodel_name="ir.model.fields",
                                        domain=[('model_id', '=',
                                                 'product.template')],
                                        string="Product Attribute")
