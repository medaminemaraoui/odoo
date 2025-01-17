from odoo import models, fields, api
from odoo.exceptions import ValidationError

class GestionLocationReservation(models.Model):
    _name = 'gestion.location.reservation'
    _description = 'Rental Reservation'

    name = fields.Char(string='Reference', required=True, copy=False, readonly=True, default='New')
    client_id = fields.Many2one('res.partner', string='Client', required=True)
    materiel_id = fields.Many2one('gestion.location.materiel', string='Material', required=True)
    date_start = fields.Date(string='Start Date', required=True)
    date_end = fields.Date(string='End Date', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft')

    rental_price = fields.Float(related='materiel_id.rental_price', string='Price per Day', store=True)
    total_days = fields.Integer(string='Total Days', compute='_compute_total_days')
    total_amount = fields.Float(string='Total Amount', compute='_compute_total_amount')

    @api.depends('date_start', 'date_end')
    def _compute_total_days(self):
        for record in self:
            if record.date_start and record.date_end:
                delta = record.date_end - record.date_start
                record.total_days = delta.days + 1
            else:
                record.total_days = 0

    @api.depends('total_days', 'rental_price')
    def _compute_total_amount(self):
        for record in self:
            record.total_amount = record.total_days * record.rental_price

    @api.constrains('date_start', 'date_end')
    def _check_dates(self):
        for record in self:
            if record.date_start and record.date_end:
                if record.date_start >= record.date_end:
                    raise ValidationError("The start date must be before the end date.")
