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

    # @api.model
    # def _get_report_values(self, docids, data=None):
    #     self.data = data
    #     report = self.env['ir.actions.report']._get_report_from_name(
    #         'product_custom_label.report_product_label')
    #
    #     return {
    #         'doc_ids': docids,
    #         'doc_model': report.model,
    #         'docs': self.env[report.model].browse(docids),
    #         # 'report_type': data.get('report_type') if data else '',
    #         # 'data': self.data,
    #         # 'get_url': self._get_url,
    #         'company': self.env.user.company_id,
    #         # 'translate_title': self._translate_title,
    #     }
