# -*- coding: utf-8 -*-
# © <2017> <Omar Torres (otorresgi18@gmail.com)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api

class evaluation(models.Model):
    _name = 'evaluation'
    _description = 'EVALUATION'

    name = fields.Char(
        string='Nombre',
        required=True
    )

    criterio = fields.Char(
        string='Criterio',
        required=True,
        size=50
    )


