from odoo import api, fields, models


class Pinjam(models.Model):
    _name = 'tokoyuki.pinjam'
    _description = 'New Description'

    pinjamdetailbuku_ids = fields.One2many(
        comodel_name='tokoyuki.pinjamdetailbuku', 
        inverse_name='pinjam_id', 
        string='Pinjam Detail Buku')

    name = fields.Char(string='Kode Order', required=True)
    tanggal_pinjam = fields.Datetime('Tanggal Pinjam',default=fields.Datetime.now())
    tanggal_pengembalian = fields.Date(string='Tanggal Pengembalian', default=fields.Date.today())
    pemesan = fields.Many2one(
        comodel_name='res.partner', 
        string='Pemesan', 
        domain=[('is_customernya', '=', True)],store=True)        

    total = fields.Integer(compute='_compute_total', string='Total', store=True)
    
    @api.depends('pinjamdetailbuku_ids')
    def _compute_total(self):
        for record in self:
            a = sum(self.env['tokoyuki.pinjamdetailbuku'].search([('pinjam_id', '=', record.id)]).mapped('harga'))
            record.total = a

    sudah_kembali = fields.Boolean(string='Sudah Dikembalikan', default=False)
    
    def kembali_barang(self):
        pass


class PinjamDetailBuku(models.Model):
    _name = 'tokoyuki.pinjamdetailbuku'
    _description = 'New Description'

    pinjam_id = fields.Many2one(
        comodel_name='tokoyuki.pinjam', 
        string='Pinjam Buku')

    buku_id = fields.Many2one(
        comodel_name='tokoyuki.buku', 
        string='Buku')

    name = fields.Char(string='Name')

    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='harga_satuan')
    
    @api.depends('buku_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.buku_id.harga

    qty = fields.Integer(string='Quantity')

    @api.constrains('qty') #untuk check kursi
    def _check_stok(self):
        for record in self:
            bahan = self.env['tokoyuki.buku'].search([('stok', '<',record.qty),('id', '=',record.id)])
            if bahan:
                raise ValidationError("Stok buku yang dipilih tidak cukup")

    harga = fields.Integer(compute='_compute_harga', string='harga')
    
    @api.depends('harga_satuan','qty') #menghitung harga
    def _compute_harga(self):
        for record in self:
            record.harga = record.harga_satuan * record.qty

    @api.model #mengurangi stok kursi tamu
    def create(self,vals):
        record = super(PinjamDetailBuku, self).create(vals) 
        if record.qty:
            self.env['tokoyuki.buku'].search([('id','=',record.buku_id.id)]).write({'stok':record.buku_id.stok-record.qty})
            return record