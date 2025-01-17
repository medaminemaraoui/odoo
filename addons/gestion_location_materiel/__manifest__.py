{
    'name': 'Gestion Location Matériel',
    'version': '1.0',
    'author': 'ibiza',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'data/notification_template.xml',
        'data/sequences.xml',
    ],
    'installable': True,
    'application': True,
}
