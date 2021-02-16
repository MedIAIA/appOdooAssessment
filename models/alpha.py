#-*- coding: utf-8 -*-

from odoo import models, fields, api
import logging as lg
import requests
from requests.exceptions import HTTPError


class Alpha(models.Model):
    _name = 'det.alpha'
    _description = 'Determinant test modèle alpha'

    @api.model
    def _default_image(self):
        image_path = get_module_resource('determinant', 'static/src/img', 'default_image.png')
        return base64.b64encode(open(image_path, 'rb').read())

    name = fields.Char(string="Nom", required=True)
    address = fields.Char(string="Adresse")
    key = fields.Char(string="Clé")
    start_date = fields.Date(string="Date de commencement")
    image = fields.Image(default=_default_image)

    def change_key(self):
        url = "https://tabatabai.dev/test_entretien/test.php?name=(:name)"
        try:
            key = requests.get(url.replace(":name", self.name))
            self.key = key.content
            # If the response was successful, no Exception will be raised
        except HTTPError as http_err:
            lg.warning('HTTP error occurred: {http_err}')
        except Exception as err:
            lg.warning('Other error occurred: {err}')
        else:
            lg.info('Success!')
