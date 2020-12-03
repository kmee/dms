# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class DmsFileInherit(models.Model):

    _inherit = 'dms.file'

    related_linked_model = fields.Selection(
        string='Linked_model',
        store=True,
        related='directory_id.linked_model')

    related_model_ids = fields.Many2many(
        comodel_name='maintenance.equipment.model',
        string='Models',
        required=False)

    related_brand_ids = fields.Many2many(
        comodel_name='maintenance.equipment.brand',
        string='Brands',
        required=False)

    related_error_ids = fields.Many2many(
        comodel_name='maintenance.error.number',
        string='Errors',
        required=False)

    related_query_ids = fields.Many2many(
        comodel_name='maintenance.equipment.query',
        string='Querys')

    related_type_ids = fields.Many2many(
        comodel_name='maintenance.equipment.type',
        string='Homologation Type')

    related_category_ids = fields.Many2many(
        comodel_name='maintenance.equipment.category',
        string='Model Categories')

    description = fields.Text(
        string="Description",
        required=False,
    )
