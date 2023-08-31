from odoo import models, api, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    def unlink(self):
        for lead in self:
            deleted_lead = self.env['custom.deleted.lead'].sudo().create({
                'lead_name': lead.name,
                'deleted_by': self.env.user.id,
                'time': fields.Datetime.now()
            })

        result = super(CrmLead, self).unlink()
        return result
