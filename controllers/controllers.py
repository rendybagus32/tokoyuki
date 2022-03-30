# -*- coding: utf-8 -*-
# from odoo import http


# class Tokoyuki(http.Controller):
#     @http.route('/tokoyuki/tokoyuki/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tokoyuki/tokoyuki/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tokoyuki.listing', {
#             'root': '/tokoyuki/tokoyuki',
#             'objects': http.request.env['tokoyuki.tokoyuki'].search([]),
#         })

#     @http.route('/tokoyuki/tokoyuki/objects/<model("tokoyuki.tokoyuki"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tokoyuki.object', {
#             'object': obj
#         })
