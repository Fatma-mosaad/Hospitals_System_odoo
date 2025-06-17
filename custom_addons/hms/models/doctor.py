from odoo import models, fields

class Doctor(models.Model):
    _name = "hms.doctor"
    _description = "Hospital Doctor"

    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    image = fields.Image()

    department_ids = fields.Many2many(
        comodel_name="hms.department",
        relation="hms_doctor_department_rel",
        column1="doctor_id",
        column2="department_id",
        string="Departments"
    )
