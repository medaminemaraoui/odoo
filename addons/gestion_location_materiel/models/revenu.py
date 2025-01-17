from odoo import models, fields

class GestionLocationRevenu(models.Model):
    _name = 'gestion.location.revenu'
    _description = 'Rental Revenue'

    name = fields.Char(string='Reference', required=True)
    date = fields.Date(string='Date', required=True, default=fields.Date.today)
    reservation_id = fields.Many2one('gestion.location.reservation', string='Reservation')
    materiel_id = fields.Many2one('gestion.location.materiel', string='Material')
    amount = fields.Float(string='Amount', required=True)
    payment_method = fields.Selection([
        ('cash', 'Cash'),
        ('bank', 'Bank Transfer'),
        ('card', 'Credit Card')
    ], string='Payment Method', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft')
