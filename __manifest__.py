{
    'name': "Customer Classification",
    'summary': """ """,
    'author': "ahmed youssef",
    'website': "",
    'sequence': -100,

    'category': '',
    'version': '0.1',
    'installable': True,
    'application': True,
    'auto_install': False,
    'depends': ['base','contacts','mail','sale_management'],

    'data': [

        'security/ir.model.access.csv',
        'views/customer_classification_views.xml',
        'views/res_partner_views_inherit.xml',
        'views/sale_report_view.xml',

    ],

}
