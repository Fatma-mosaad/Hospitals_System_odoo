# -*- coding: utf-8 -*-
{
    "name": "Hospital Management System",
    "version": "1.0",
    "summary": "Manage hospital patients",
    "description": """
This module manages patient records in a hospital.
    """,
    "author": "Fatma",
    "website": "https://www.yourcompany.com",
    "category": "Healthcare",
    "depends": ["base"],
   "data": [
    "security/ir.model.access.csv",
    "views/hms_actions.xml",
    "views/menu.xml",               
    "views/patient_views.xml",
    "views/department_views.xml",
    "views/doctor_views.xml",
],

    "demo": [],
    "installable": True,
    "application": True,
    "auto_install": False,
}
