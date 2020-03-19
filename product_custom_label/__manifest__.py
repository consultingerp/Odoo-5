# -*- coding: utf-8 -*-
{
    'name':
    "Product Custom Label",
    'author':"adre",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '12.0.1.0.4',
    'description':
    """
    Module allows to print custom product labels on different paper formats.
    Label size: 57x35mm, paperformat: A4 (21 pcs per sheet, 3 pcs x 7 rows).
        """,

    # any module necessary for this one to work correctly
    'depends': ['product', 'web_widget_colorpicker'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/stock_product_tag_views.xml',
        'views/product_template_views.xml',
        'wizard/print_product_label_views.xml',
        'report/product_label_templates.xml',
        'report/product_label_reports.xml',
        'views/template.xml',
        'data/stock_product_tag_data.xml',
        'views/menus.xml',
    ],
	'application': False,
    'installable': True,
    'auto_install': False,
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
