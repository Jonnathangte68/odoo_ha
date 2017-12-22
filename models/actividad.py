# -*- coding: utf-8 -*-
# © <2017> <Omar Torres (otorresgi18@gmail.com)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api

class actividad(models.Model):
    _name = 'actividad'
    _description = 'ACTIVIDAD'

    name = fields.Char(
        string='Nombre',
        required=True
    )
    '''
        ghda_id = fields.Many2one (
            string='Actividad',
            comodel_name='ghda',
            inverse_name='actividad_ids'
        )
    '''
    um = fields.Selection(
        string='UM*',
        selection=[('min', 'Min'), ('nummin', '# / Min')]
    )

    frecuencia = fields.Char(
        string='Frecuencia',
        help='Mintos x dia',
        size=50
    )

    lunes = fields.Boolean(
        string='Lunes'
    )

    martes = fields.Boolean(
        string='Martes'
    )

    miercoles = fields.Boolean(
        string='Miercoles'
    )

    jueves = fields.Boolean(
        string='Jueves'
    )

    viernes = fields.Boolean(
        string='Viernes'
    )

    sabado = fields.Boolean(
        string='Sabado'
    )
