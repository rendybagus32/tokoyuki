from odoo import http, fields, models
from odoo.http import request
import json


class BukuCon(http.Controller):
        @http.route(['/buku','/buku/<int:idnya>'], auth='public', methods=['GET'], csrf=True)
        def getBuku(self, idnya=None, **kwargs):
            value = []
            if not idnya:
                kursi = request.env['tokoyuki.buku'].search([])            
                for k in kursi:
                    value.append({"id" : k.id,
                                "nama_buku" : k.name,
                                "stok_tersedia" : k.qty,
                                "harga_beli" : k.harga})
                return json.dumps(value)
            else:
                kursiid = request.env['tokoyuki.buku'].search([('id','=',idnya)])
                for k in kursiid:
                    value.append({"id" : k.id,
                                "nama_buku" : k.name,
                                "stok_tersedia" : k.qty,
                                "harga_beli" : k.harga})
                return json.dumps(value)

        @http.route('/createbuku',auth='user', type='json', methods=['POST'])
        def createKursi(self, **kw):
            if request.jsonrequest:
                if kw['name']:
                    vals = {
                        'name' : kw['name'], 
                        'qty' : kw['qty'],
                        'harga' : kw['harga'],
                    }
                    bukubaru = request.env['tokoyuki.buku'].create(vals)
                    args = {'succeed': True, "ID" : bukubaru.id}
                    return args