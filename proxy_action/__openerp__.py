# -*- encoding: utf-8 -*-
##############################################################################
#
#    Model module for OpenERP
#    Copyright (C) 2010 Sébastien BEAU <sebastien.beau@akretion.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{'name': 'Proxy Action',
 'version': '0.0.1',
 'author': 'Akretion',
 'website': 'www.akretion.com',
 'license': 'AGPL-3',
 'category': 'Generic Modules',
 'description': """This module will help you to integrate direct printing
 application using pywebdriver with cups
 """,
 'depends': [
     'base',
 ],
 'data': [
 ],
 'js': [
     'static/src/js/view.js'
 ],
 'installable': True,
 'application': False,
 }
