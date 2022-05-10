import codecs
codecs.open('', encoding='utf-8')

# -*- coding: utf-8 -*-
from odoo import models, fields, api

class product_template(models.Model):
    _inherit = "product.template"

    @api.multi
    def name_get(self):
        res = []
        for rec in self:
            name = rec.name
            if rec.default_code:
                name = rec.default_code + '-' + name
            res.append((rec.id, name))
        return res
