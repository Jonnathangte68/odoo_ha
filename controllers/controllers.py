# -*- coding: utf-8 -*-
from odoo import http

# class Ghda(http.Controller):
#     @http.route('/ghda/ghda/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ghda/ghda/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ghda.listing', {
#             'root': '/ghda/ghda',
#             'objects': http.request.env['ghda.ghda'].search([]),
#         })

#     @http.route('/ghda/ghda/objects/<model("ghda.ghda"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ghda.object', {
#             'object': obj
#         })