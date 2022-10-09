# -*- coding: utf-8 -*-
# from odoo import http


# class Component(http.Controller):
#     @http.route('/component/component', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/component/component/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('component.listing', {
#             'root': '/component/component',
#             'objects': http.request.env['component.component'].search([]),
#         })

#     @http.route('/component/component/objects/<model("component.component"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('component.object', {
#             'object': obj
#         })
