# -*- coding: utf-8 -*-
# Copyright 2009-2018 Aurium Technologies.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class PricelistLine(models.Model):
    _inherit = 'product.pricelist.item'

    @api.model
    def _report_xls_fields(self):
        """
        Adapt list in custom module to add/drop columns or change order.
        """
        return [
           # 'product_id',
        ]

    @api.model
    def _report_xls_template(self):
        """
        Template updates, e.g.

        tmpl_upd = super(PricelistLine, self)._report_xls_template()
        tmpl_upd.update({
            'note': {
                'header': [1, 42, 'text', _render("_('Notes')")],
                'lines': [1, 0, 'text', _render("line.note or ''")],
                'totals': [1, 0, 'text', None]},
        }
        return tmpl_upd
        """
        return {}
