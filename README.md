# Project Cost Estimations Management

Professional custom Odoo module to manage project cost estimates and approvals. Compatible with **Odoo 18 Enterprise**.


Summary
- Create and manage project cost estimates with breakdown lines.
- Lightweight approval workflow: `draft → submitted → approved/rejected`.
- Email notifications on approve/reject using a predefined mail template.
- Integrated with Odoo mail thread and activity mixin for collaboration.

Compatibility
- Odoo: 18 Enterprise
- Languages & tools used: Python, JavaScript, TypeScript, SQL, C (native libs possible), pip

Key features
- Models:
  - `project.cost.estimate` — estimate header, computed `estimated_total_cost`, `state` (tracking enabled).
  - `breakdown.line` — one-to-many lines with `cost`.
  - Extends `project.project` to include `cost_estimate_ids` and computed `latest_cost_estimate`.
- Views: kanban, list, form (with state-based read-only rules), notebook with editable breakdown lines.
- Menu & action: `Project Cost` main menu and action `action_project_cost_estimate`.
- Email template: `project_cost_estimations_management.email_template_cost_estimate_state`.
- Security:
  - Groups: `project_cost_estimations_management.group_project_user`, `group_project_admin`, `group_approval_group`.
  - Access rights defined in `security/ir.model.access.csv`.
  - Record rules to restrict users to own estimates, admins to projects they manage, approval group to `submitted` records.



Configuration
- Mail: configure outgoing mail server in Odoo to enable notifications.
- Access & groups: review `security/security.xml` and `security/ir.model.access.csv` to map users to groups.
- Templates & translations: review `data/mail_template.xml` and add translations if required.

Usage
- Create a new Project Cost Estimate, add Breakdown Lines (name + cost).
- Use `Submit` to lock basic fields and `Approve` / `Reject` (approval group only).
- Approve/Reject triggers the email template and logs chatter messages.

Developer notes
- Main files of interest:
  - `__manifest__.py`
  - `models/project_cost_estimate.py`
  - `models/project_project.py`
  - `views/project_cost_estimate_view.xml`
  - `views/project_view_inherit.xml`
  - `data/mail_template.xml`
  - `security/security.xml`
  - `security/ir.model.access.csv`
- Recommended environment: Windows, PyCharm 2025.2.2, Odoo 18 Enterprise.
- Use developer mode in Odoo for view debugging and access rights testing.
- Use PyCharm to run and debug; run Odoo with `--dev=xml,sql` for faster view reloads during development.

