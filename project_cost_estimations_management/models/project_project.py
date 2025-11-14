from odoo import models, fields, api

class ProjectProject(models.Model):
    _inherit = 'project.project'
    cost_estimate_ids = fields.One2many(
        "project.cost.estimate", "project_id", string="Cost Estimates"
    )

    latest_cost_estimate = fields.Float(
        compute="_compute_latest_cost_estimate",
        store=True
    )
    def action_view_cost_estimates(self):
        return {
            'name': 'Cost Estimates',
            'type': 'ir.actions.act_window',
            'res_model': 'project.cost.estimate',
            'view_mode': 'list,form,kanban',
            'domain': [('project_id', '=', self.id)]
        }

    @api.depends("cost_estimate_ids.estimated_total_cost", "cost_estimate_ids.create_date")
    def _compute_latest_cost_estimate(self):
        for project in self:
            estimate = self.env["project.cost.estimate"].search(
                [("project_id", "=", project.id)],
                order="create_date desc",
                limit=1
            )
            project.latest_cost_estimate = estimate.estimated_total_cost if estimate else 0.0