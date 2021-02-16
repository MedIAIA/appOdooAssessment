# -*- coding: utf-8 -*-
# from odoo import http


# class Determinant(http.Controller):
#     @http.route('/determinant/determinant/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/determinant/determinant/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('determinant.listing', {
#             'root': '/determinant/determinant',
#             'objects': http.request.env['determinant.determinant'].search([]),
#         })

#     @http.route('/determinant/determinant/objects/<model("determinant.determinant"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('determinant.object', {
#             'object': obj
#         })
