# -*- coding: utf-8 -*-
# © <2017> <Omar Torres (otorresgi18@gmail.com)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api

class ghda(models.Model):
    _name = 'ghda'
    _description = 'GHDA'

    name = fields.Char(
        string='Nombre',
        required=True
    )
    '''
        actividad_id = fields.one2Many(
            string='Hoja de actividad',
            comodel_name='actividad',
        )
    '''