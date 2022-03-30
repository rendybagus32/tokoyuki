from odoo import api, fields, models


class Buku(models.Model):
    _name = 'tokoyuki.buku'
    _description = 'New Description'

    name = fields.Char(string='Judul', required=True)
    qty = fields.Integer(string='Stok Buku')
    harga = fields.Integer(string='Harga Sewa Buku')