#!/usr/bin/python
#-*-coding:utf-8-*-
#- translate Class

#- Copyright (C) 2014 GoldraK & Interhack 
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License 
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. 
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty 
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. 
# You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>

# WebSite: http://adminserver.org/
# Email: contacto@adminserver.org
# Facebook: https://www.facebook.com/pages/Admin-Server/795147837179555?fref=ts
# Twitter: https://twitter.com/4dminserver

import gettext

class translate(object):
	@staticmethod

	#- le pasamos el nombre del archivo de traduccion
	def init(traduccion, path=''):
		try:
			if path == '':
				t = gettext.translation(traduccion, 'locale')
			else:
				t = gettext.translation(traduccion, path)
		except:
			if path == '':
				t = gettext.translation(traduccion, 'locale', languages=['en_US'])
			else:
				t = gettext.translation(traduccion, path, languages=['en_US'])
		return t