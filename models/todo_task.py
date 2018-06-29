# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TodoTask(models.Model):
    _name = 'todo.task'
    _inherit = ['todo.task', 'mail.thread']

    user_id = fields.Many2one('res.users', 'Assigned to')
    deadline_date = fields.Date('Deadline')
    name = fields.Char(help="Cosa bisogna fare?")

    @api.multi
    def do_clear_done(self):
        dones = self.search([
            ('is_done', '=', True),
            '|', ('user_id', '=', self.env.uid),
                ('user_id', '=', False)
        ])

        dones.write({'active': False})

    
    @api.multi
    def do_toggle_done(self):
        for task in self:
            if tast.user_id != self.env.user:
                raise ValidationError("Solo l'incaricato può chiudere questo task")

        return super(TodoTask, self).do_toggle_done()