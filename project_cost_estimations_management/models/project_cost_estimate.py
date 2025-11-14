from odoo import models, fields, api


class ProjectCostEstimate(models.Model):
    _name = "project.cost.estimate"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char()
    project_id = fields.Many2one('project.project')
    breakdown_ids = fields.One2many("breakdown.line", "estimate_id")
    estimated_total_cost = fields.Float(compute='_estimated_total_cost', store=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], default='draft', tracking=True)


    @api.depends('breakdown_ids.cost')
    def _estimated_total_cost(self):
        for rec in self:
            rec.estimated_total_cost = sum(rec.breakdown_ids.mapped('cost'))

    def action_submit(self):
        self.write({'state': 'submitted'})


    def action_approve(self):
        self.write({'state': 'approved'})
        self._send_state_email()

    def action_reject(self):
        self.write({'state': 'rejected'})
        self._send_state_email()

    def _send_state_email(self):
        template = self.env.ref('project_cost_estimations_management.email_template_cost_estimate_state')
        self.env['mail.template'].browse(template.id).send_mail(self.id, force_send=True)

class BreakdownLines(models.Model):
    _name = "breakdown.line"
    name = fields.Char()
    cost = fields.Float()
    estimate_id = fields.Many2one("project.cost.estimate")
