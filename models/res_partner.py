from odoo import api, fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    # NIM = fields.Integer(string='NIM')
    # NamaMahasiswa = fields.Char(string='NamaMahasiswa')
    # Jurusan = fields.Char(string='Jurusan')
    # Fakultas = fields.Char(string='Fakultas')
    # Angkatan = fields.Char(string='Angkatan')
    is_mahasiswa = fields.Boolean(string='mahasiswa', default=False)
    