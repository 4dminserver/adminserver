#!/usr/bin/python
#-*-coding:utf-8-*-
#- newModule Class

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

import os, subprocess


class newModule(object):
	def __init__(self, nameModule, output, translate, log, installer):

		interpret = translate.init('newModule')
		_ = interpret.ugettext

		try:
			from datetime import date

			day = date.today()
			date = str(day.year) + '-' + str(day.month) + '-' + str(day.day)

			if not os.path.exists('modules/' + str(nameModule)):
				os.makedirs('modules/' + str(nameModule))
				module = open('modules/' + str(nameModule) + '/' + 'ini_' + str(nameModule) + '.py', 'w')
				module.write("""#!/usr/bin/python
#-*-coding:utf-8-*-
#- """ + nameModule + """ Class

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

#- imports necessary

class add(object):

	#- @output.[option](default, error)(text) -> printed by stdout
	#- @translate.[option](init('nameTranslate')) -> initializes the translation file
	#- @log.[option](write)(text,*1) -> 1 is error -> saves information in the logs
	#- @installer -> module for install dependencies -> nonoperating

	def __init__(self, output, translate, log, installer, options):
		#- Operations
		#- Example:
		output.default('Hello World!!!')

class help(object):
	@staticmethod
	#- @translate.[option](init('nameTranslate')) -> initializes the translation file
	def info(translate):
		return 'NewModule Example Hello World'

	@staticmethod
	#- Especificamos si necesita el modulo paquetes adicionales.
	def package():
		#- List of extra dependencies needed by the module
		addtionalPackage = []
		return additionalPackage""")
				msg = _('New module created successfully')
				output.default(msg)
				log.write(msg)
				module.close()
			else:
				msg = _('There is a module with the same module')
				output.default(msg)
				log.write(msg, 1)
		except:
			msg = _('Error writing the new module')
			output.error(msg)
			log.write(msg, 1)

class newModuleMenu(object):
	def __init__(self, nameModule, output, translate, log, installer):
		interpret = translate.init('newModuleMenu')
		_ = interpret.ugettext

		try:
			from datetime import date

			day = date.today()
			date = str(day.year) + '-' + str(day.month) + '-' + str(day.day)

			if not os.path.exists('modules/' + str(nameModule)):
				os.makedirs('modules/' + str(nameModule))
				module = open('modules/' + str(nameModule) + '/' + 'ini_' + str(nameModule) + '.py', 'w')
				module.write("""#!/usr/bin/python
#-*-coding:utf-8-*-
#- """ + nameModule + """ Class

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

#- imports necessary

class add(object):

	#- @output.[option](default, error)(text) -> printed by stdout
	#- @translate.[option](init('nameTranslate')) -> initializes the translation file
	#- @log.[option](write)(text,*1) -> 1 is error -> saves information in the logs
	#- @installer -> module for install dependencies -> nonoperating

	def __init__(self, output, translate, log, installer,options):
		#- Operations
		#- Example:
		output.default('Hello World Menu!!!')
		def __menu__():
			output.default('Opcion 1')
			output.default('Opcion 2')
			output.default('exit ==> 0')

		def option1():
			output.default('Has seleccionado la opcion 1')
		
		def option2():
			output.default('Has seleccionado la opcion 2')
		
		__menu__()

		control = True
		while control == True:
			options.set_completer(help.complete)
			sentencia = raw_input("prueba >> ")
			if sentencia == '1':
				option1()
			elif sentencia == '2':
				option2()
			elif sentencia == '0':
				control = False
			elif sentencia == 'exit':
				control = False
			elif sentencia == 'version':
				output.default(help.version())
			elif sentencia == 'help':
				output.default(help.help())
			else:
				output.default('No ha seleccionado una opcion correcta')

class help(object):
	#- Commands default
	@staticmethod
	def complete(text, state):
		possibilities = ["exit", "version", "help"]
		results = [x for x in possibilities if x.startswith(text)] + [None]
		return results[state]

	#- Help for menu
	@staticmethod
	def help(translate=''):
		return "Help Module"

	@staticmethod
	def version(translate=''):
		return "Version 0.1"

	@staticmethod
	#- @translate.[option](init('nameTranslate')) -> initializes the translation file
	def info(translate):
		return 'NewModule Example Hello World'

	@staticmethod
	#- Especificamos si necesita el modulo paquetes adicionales.
	def package():
		#- List of extra dependencies needed by the module
		addtionalPackage = []
		return additionalPackage""")
				msg = _('New module created successfully')
				output.default(msg)
				log.write(msg)
				module.close()
			else:
				msg = _('There is a module with the same module')
				output.default(msg)
				log.write(msg, 1)
		except:
			msg = _('Error writing the new module')
			output.error(msg)
			log.write(msg, 1)


class createModule(object):
	@staticmethod
	def compileModule(nameModule,output,translate,log):
		if not os.path.exists('compiles'):
			os.makedirs('compiles')

		commandCompress = 'tar czvf compiles/' + nameModule + '.asm modules/' + nameModule
		compress = subprocess.Popen(commandCompress, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		#- Lee si ha ocurrido un error
		compress_error = compress.stderr.read()
		compress_stdout = compress.stdout.read()
		if compress_stdout != '':
			msg = 'Error al compilar el modulo: ' + compress_error
			log.write(msg, 1)
			output.error(msg)
		else:
			output.default('Compilando....')
			output.default(compress_error)
			msg = 'Modulo Compilado Correctamente: ' + nameModule + '\n'
			log.write(msg)
			output.default(msg)

	@staticmethod
	def decompileModule(nameModule, output, translate, log):
		commandLookCompile = 'tar tzf ' + nameModule
		lookCompile = subprocess.Popen(commandLookCompile, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		module = lookCompile.stdout.readline().split('/')[1]

		if not os.path.exists('modules/' + str(module)):
			commandDecompile = 'tar xzvf ' + nameModule
			decompile = subprocess.Popen(commandDecompile, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
			decompile_error = decompile.stderr.read()
			decompile_stdout = decompile.stdout.read()
			if decompile_stdout != '':
				msg = 'Error al instalar el modulo: ' + str(nameModule)
				log.write(msg, 1)
				output.error(msg)
			else:
				output.default('Instalando....')
				output.default(decompile_error)
				msg = 'Modulo instalado correctamente: ' + str(nameModule) + '\n'
				log.write(msg)
				output.default(msg)
		else:
			output.error('Ya existe el modulo instalado')