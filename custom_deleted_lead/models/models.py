# -*- coding: utf-8 -*-

from odoo import models, fields, api
class CustomDeletedLead(models.Model):
    _name = 'custom.deleted.lead'
    _description = 'Deleted Leads'

    lead_name = fields.Char(string='Lead Name')
    deleted_by = fields.Many2one('res.users', string='Deleted By')
    time = fields.Datetime(string='Deleted At')

# class custom_deleted_lead(models.Model):
#     _name = 'custom_deleted_lead.custom_deleted_lead'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
