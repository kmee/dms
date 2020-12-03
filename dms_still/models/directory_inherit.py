# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _

LINKED_MODEL = [
    ('service_info', 'Service Information'),
    ('tot_videos', 'TOT Videos'),
    ('technical_doc', 'Technical Documentation'),
    ('matriculation', 'Matriculation'),
    ('procedures', 'Procedures'),
    ('normative', 'Normative'),
    ('technical_analysis', 'Technical analysis')
]


class DirectoryInherit(models.Model):

    _inherit = 'dms.directory'

    linked_model = fields.Selection(
        string='Linked Model',
        selection=LINKED_MODEL,
        required=False,
    )


    @api.model
    def create(self, vals):
        res = super(DirectoryInherit, self).create(vals)
        if res.parent_id:
            res.linked_model = res.parent_id.linked_model

        return res
