# -*- coding: utf-8 -*-
from odoo import http

# class SfMassPayment(http.Controller):
#     @http.route('/sf_mass_payment/sf_mass_payment/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sf_mass_payment/sf_mass_payment/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sf_mass_payment.listing', {
#             'root': '/sf_mass_payment/sf_mass_payment',
#             'objects': http.request.env['sf_mass_payment.sf_mass_payment'].search([]),
#         })

#     @http.route('/sf_mass_payment/sf_mass_payment/objects/<model("sf_mass_payment.sf_mass_payment"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sf_mass_payment.object', {
#             'object': obj
#         })