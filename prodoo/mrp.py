# -*- coding: utf-8 -*-
###############################################################################
#
#   Module for OpenERP
#   Copyright (C) 2014 Akretion (http://www.akretion.com).
#   @author Sébastien BEAU <sebastien.beau@akretion.com>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from openerp import models, api


class MrpProduction(models.Model):
    _inherit='mrp.production'

    @api.multi
    def prodoo_produce(self):
        wizard_obj = self.env['mrp.product.produce']
        for mo in self:
            wiz = wizard_obj.with_context({'active_id': mo.id}).create({})
            vals = wiz.on_change_qty(wiz.product_qty, [])
            wiz.write({'consume_lines': vals['value']['consume_lines']})
            self.force_production()
            mo.action_produce(mo.id, wiz.product_qty, wiz.mode, wiz=wiz)
        return True
#        proxy_obj = self.env['proxy.action.helper']
#        action = self.env['proxy.action.helper'].get_print_report_action(
#            'report.mrp.production.label', 'mrp.production', [mo.id])
#        return proxy_obj.return_action([action])
