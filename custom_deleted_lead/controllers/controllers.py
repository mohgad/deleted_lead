# -*- coding: utf-8 -*-
from odoo import http

# class CustomDeletedLead(http.Controller):
#     @http.route('/custom_deleted_lead/custom_deleted_lead/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_deleted_lead/custom_deleted_lead/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_deleted_lead.listing', {
#             'root': '/custom_deleted_lead/custom_deleted_lead',
#             'objects': http.request.env['custom_deleted_lead.custom_deleted_lead'].search([]),
#         })

#     @http.route('/custom_deleted_lead/custom_deleted_lead/objects/<model("custom_deleted_lead.custom_deleted_lead"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_deleted_lead.object', {
#             'object': obj
#         })