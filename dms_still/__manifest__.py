# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'DMS Still',
    'description': """
        Add Links with system models""",
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'KMEE',
    'website': 'kmee.com.br',
    'depends': [
        'dms',
        'still_equipment',
        'still_matriculation',
    ],
    'data': [
        'views/directory_inherit.xml',
        'views/dms_file_inherit.xml',
    ],
    'demo': [
    ],
}
