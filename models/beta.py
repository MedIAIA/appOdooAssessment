#-*- coding: utf-8 -*-

from odoo import models, fields, api


class Beta(models.Model):
    _name = 'det.beta'
    _description = 'determinant test modèle beta'

    name = fields.Char(string="Nom",  required=True)
    phone = fields.Char(string="Téléphone")
    price = fields.Float(string="Prix")
    alpha_id = fields.Many2one('det.alpha', string="Alpha", ondelete='cascade', store=True)

