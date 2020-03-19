# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import Warning


class PrintProductLabel(models.TransientModel):
    _name = "print.product.label"
    _description = 'Product Labels Wizard'

    # TODO:  tests - try_report_action

    @api.model
    def _get_products(self):
        res = []
        if self._context.get('active_model') == 'product.template':
            products = self.env[self._context.get('active_model')].browse(self._context.get('default_product_ids'))
            for product in products:
                label = self.env['print.product.label.line'].create({
                    'product_id': product.product_variant_id.id,
                })
                res.append(label.id)
        elif self._context.get('active_model') == 'product.product':
            products = self.env[self._context.get('active_model')].browse(self._context.get('default_product_ids'))
            for product in products:
                label = self.env['print.product.label.line'].create({
                    'product_id': product.id,
                })
                res.append(label.id)
        return res

    name = fields.Char(
        'Name',
        default='Print product labels',
    )
    message = fields.Char(
        'Message',
        readonly=True,
    )
    output = fields.Selection(
        selection=[('pdf', 'PDF')],
        string='Print to',
        default='pdf',
    )
    label_ids = fields.One2many(
        comodel_name='print.product.label.line',
        inverse_name='wizard_id',
        string='Labels for Products',
        default=_get_products,
    )
    template_id = fields.Many2one(
        comodel_name="stock.product.tag",
        string="Template labels",
        required=True,
        default=lambda self: self.env['stock.product.tag'].search([], limit=1).id
    )
    qty_per_product = fields.Integer(
        string='Label quantity per product',
        default=1,
    )
    humanreadable = fields.Boolean(
        string='Print digital code of barcode',
        default=False,
    )

    @api.multi
    def action_print(self):
        """ Print labels """
        self.ensure_one()
        labels = self.label_ids.filtered(lambda x: x.selected == True and x.qty > 0).mapped('id')
        print(labels, 'labels')
        if not labels:
            raise Warning(_('Nothing to print, set the quantity of labels in the table.'))

        data = {
            'ids': self.ids,
            'form': {
                'labels': labels,
                'template': self.template_id.id,
            },
        }
        print(data)

        return self.env.ref(self.template_id.template)\
            .with_context(discard_logo_check=True).report_action(self, data=data)

        # return self.env.ref(self.template_id.template).with_context(discard_logo_check=True).report_action(labels)

    @api.multi
    def action_set_qty(self):
        self.ensure_one()
        self.label_ids.write({'qty': self.qty_per_product})

    @api.multi
    def action_restore_initial_qty(self):
        self.ensure_one()
        for label in self.label_ids:
            if label.qty_initial:
                label.update({'qty': label.qty_initial})
