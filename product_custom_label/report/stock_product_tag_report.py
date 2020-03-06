# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models


class ProductTagReport(models.AbstractModel):
    _name = 'report.product_custom_label.report_product_label_view'
    _description = 'Stock Product Tag Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        labels = data['form']['labels']
        template = data['form']['template']

        product_tag = self.env['stock.product.tag'].browse(template)
        product_labels = self.env['product.label'].browse(labels)

        labels = [label for label in product_labels]
        print(labels)

        docs = {
            'product_tag': product_tag,
            'labels': labels,
        }

        return {
            'doc_ids': data['ids'],
            'docs': docs,
        }


class ProductTagReport2(models.AbstractModel):
    _name = 'report.product_custom_label.report_product_label_2_view'
    _description = 'Stock Product Tag Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        labels = data['form']['labels']
        template = data['form']['template']

        product_tag = self.env['stock.product.tag'].browse(template)
        product_labels = self.env['product.label'].browse(labels)

        labels = [label for label in product_labels]
        print(labels)

        docs = {
            'product_tag': product_tag,
            'labels': labels,
        }

        return {
            'doc_ids': data['ids'],
            'docs': docs,
        }


class ProductTagReport3(models.AbstractModel):
    _name = 'report.product_custom_label.report_product_label_3_view'
    _description = 'Stock Product Tag Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        labels = data['form']['labels']
        template = data['form']['template']

        product_tag = self.env['stock.product.tag'].browse(template)
        product_labels = self.env['product.label'].browse(labels)

        labels = [label for label in product_labels]
        print(labels)

        docs = {
            'product_tag': product_tag,
            'labels': labels,
        }

        return {
            'doc_ids': data['ids'],
            'docs': docs,
        }


class ProductTagReport4(models.AbstractModel):
    _name = 'report.product_custom_label.report_product_label_4_view'
    _description = 'Stock Product Tag Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        labels = data['form']['labels']
        template = data['form']['template']

        product_tag = self.env['stock.product.tag'].browse(template)
        product_labels = self.env['product.label'].browse(labels)

        labels = [label for label in product_labels]
        print(labels)

        docs = {
            'product_tag': product_tag,
            'labels': labels,
        }

        return {
            'doc_ids': data['ids'],
            'docs': docs,
        }
