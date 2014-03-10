#!/usr/bin/python
#-*-coding:utf-8-*-

#- AdminServer / System Management Server
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

#- Importamos los modulos necesarios

import sys, os, readline

#- Incluye las classes necesarias para el core del programa
sys.path.append('model')
from translate import translate
from utilidades import salida
from utilidades import sistema, log, helpSystem, installer
from easter import easter

#- Iniciamos comprobación de usuario
sistema.userSystem(salida)

#- Llamamos a la clase translate para inicializar el archivo traduccion init
interpret = translate.init('init')
_ = interpret.ugettext

#- Inicializamos la clase installer
installer = installer(salida, translate, log)

#- Inicializamos el Autocompletado
readline.parse_and_bind("tab: complete")

salida.default(sistema.promptInit())

salida.default(_("Welcome to Server Configurator") + ' / JarJar')
salida.default("")
salida.default(_("Available options:") + "\n")

#- Incluye los modulos que puede tener el programa
menu = sistema.explorar('modules')
for items in menu:
	salida.default(str(items) + ' - ' + str(menu[items]))

salida.default("")
elements_menu = len(menu)

#- Bucle infinito que nos muestra el prompt
while True:
	readline.set_completer(helpSystem.complete)
	sentencia = raw_input("adminServer >> ")
	try:
		if sentencia.split(' ')[0] == 'newmodule':
			try:
				newmodule = sentencia.split(' ')[1]
				try:
					sys.path.append('model')
					from newModule import newModule
					newModule(newmodule, salida, translate, log, 'installer')
				except:
					msg = _('Fatal Error in create new module')
					salida.error(msg)
					log.write(msg, 1)
			except IndexError:
				msg = _('You need to specify a name for module')
				salida.error(msg)
				log.write(msg, 1)

		elif sentencia == 'linux':
			salida.default(easter.linux())

		elif sentencia.split(' ')[0] == 'newmodulemenu':
			try:
				newmodule = sentencia.split(' ')[1]
				try:
					sys.path.append('model')
					from newModule import newModuleMenu
					newModuleMenu(newmodule, salida, translate, log, 'installer')
				except:
					msg = _('Fatal Error in create new module')
					salida.error(msg)
					log.write(msg, 1)
			except IndexError:
				msg = _('You need to specify a name for module')
				salida.error(msg)
				log.write(msg, 1)

		elif sentencia == 'modules':
			#- Incluye los modulos que puede tener el programa
			menu = sistema.explorar('modules')
			for items in menu:
				salida.default(str(items) + ' - ' + str(menu[items]))
				elements_menu = len(menu)

		elif sentencia.split(' ')[0] == 'help':
			try:
				opcion = sentencia.split(' ')[1]
				newHelp = menu[int(opcion)]
				helpSystem.info(salida,translate,log, newHelp)
			except:
				helpSystem.info(salida, translate, log)
		elif sentencia == 'clear':
			sistema.clear()
		elif sentencia == 'license':
			sistema.license(salida)
		elif sentencia == 'version':
			sistema.version(salida)
		elif sentencia.split(' ')[0] == 'install':
			try:
				opcion = sentencia.split(' ')[1]
				from newModule import createModule
				createModule.decompileModule(opcion, salida, translate, log)
			except:
				salida.error('You need put a name module')

		elif sentencia.split(' ')[0] == 'compile':
			try:
				opcion = sentencia.split(' ')[1]
				compileModule = menu[int(opcion)]
				from newModule import createModule
				createModule.compileModule(compileModule, salida, translate, log)
			except:
				salida.error('You need put a name module')
		
		elif sentencia == 'exit':
			exit()

		elif int(sentencia) <= int(elements_menu):
			try:
				opcion = menu[int(sentencia)]
				ruta = 'modules/' + opcion
				sys.path.append(ruta)
				try:
					module = __import__('ini_' + opcion)
					module.add(salida, translate, log, 'installer')
					menu = sistema.explorar('modules')
					for items in menu:
						salida.default(str(items) + ' - ' + str(menu[items]))
						elements_menu = len(menu)
				except:
					msg = _("Error in module ") + opcion
					salida.error(msg);log.write(msg, 1)
			except KeyError:
				msg = _("Option invalid")
				salida.error(msg);log.write(msg, 1)
		else:
			msg = _("Option invalid")
			salida.default(msg);log.write(msg, 1)
	except ValueError:
		msg = _("Need to put a number")
		salida.error(msg);log.write(msg, 1)