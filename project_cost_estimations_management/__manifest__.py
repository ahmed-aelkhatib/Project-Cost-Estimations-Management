{
    "name": "Project Cost Estimations Management",
    "summary": "Module for manages Project Cost Estimations.",
    "version": "1.0",
    "depends": ['base', 'project',"mail"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/menu_items_view.xml",
        "data/mail_template.xml",
        "views/project_cost_estimate_view.xml",
        "views/project_view_inherit.xml"

    ],
    "application": True,
    "installable": True,
}
