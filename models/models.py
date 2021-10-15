# -*- coding: utf-8 -*-

from odoo import models, fields, api


class clinic(models.Model):
    _name = 'clinic.clinic'
    _description = 'Clinic'

    name = fields.Char(string="Nama")
    description = fields.Char(string="Description")

