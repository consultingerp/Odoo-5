# -*- coding: utf-8 -*-
from odoo import http

# class StockCustomLabel(http.Controller):
#     @http.route('/stock_custom_label/stock_custom_label/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_custom_label/stock_custom_label/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_custom_label.listing', {
#             'root': '/stock_custom_label/stock_custom_label',
#             'objects': http.request.env['stock_custom_label.stock_custom_label'].search([]),
#         })

#     @http.route('/stock_custom_label/stock_custom_label/objects/<model("stock_custom_label.stock_custom_label"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_custom_label.object', {
#             'object': obj
#         })