# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Product Price History',
    'version': '12.0',
    'category': 'Purchases',
    'author':'Aurium Technologies',
    'description': """
      Add a products price history list and graph view
    """,
    'website': 'http://auriumtechnologies.com',
    'depends': ['purchase'],
    'data': [
        'views/product_price_history_view.xml', 
    ],
    
    'installable': True,
    'auto_install': False,
    'license': 'AGPL-3',
}
