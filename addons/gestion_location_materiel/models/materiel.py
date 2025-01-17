from odoo import models, fields

class GestionLocationMateriel(models.Model):
    _name = 'gestion.location.materiel'
    _description = 'Material Management'

    name = fields.Char(string='Name', required=True)
    reference = fields.Char(string='Reference', required=True)
    description = fields.Text(string='Description')
    category = fields.Selection([
        ('tools', 'Tools'),
        ('equipment', 'Equipment'),
        ('machinery', 'Machinery')
    ], string='Category', required=True)
    rental_price = fields.Float(string='Rental Price', required=True)
    availability = fields.Boolean(string='Available', default=True)
    state = fields.Selection([
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('maintenance', 'Under Maintenance')
    ], string='Status', default='available')
