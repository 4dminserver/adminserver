#!/usr/bin/python
#-*-coding:utf-8-*-
#- teco System

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

import os, sys

# Colores en las letras

magenta = '\033[95m'
azul = '\033[94m'
verde = '\033[92m'
amarillo = '\033[93m'
rojo = '\033[91m'
cyan = '\033[36m'
blanco = '"\033[37m'
negro = '\033[30m'

# Colores en los fondos de las letras

bverde = '\033[42m'
bcyan = '\033[45m'
bblanco = '\033[47m'
bnegro = '\033[40m'
bamarillo = '\033[43m'
bazul = '\033[44m'
brojo = '\033[41m'
bmagenta = '\033[45m'

# Especiales

negrita = '\033[1m'
reverse = '\033[7m'
subrallado = '\033[4m'

# Fin de formato

end = '\033[0m'

def color(color, string):

	if color == 'magenta':
		return magenta+string+end
	elif color == 'azul':
		return azul+string+end
	elif color == 'verde':
		return verde+string+end
	elif color == 'amarillo':
		return amarillo+string+end
	elif color == 'rojo':
		return rojo+string+end
	elif color == 'cyan':
		return cyan+string+end
	elif color == 'blanco':
		return blanco+string+end
	elif color == 'negro':
		return negro+string+end
	elif color == 'bverde':
		return bverde+string+end
	elif color == 'bcyan':
		return bcyan+string+end
	elif color == 'bblanco':
		return bblanco+string+end
	elif color == 'bnegro':
		return bnegro+string+end
	elif color == 'bamarillo':
		return bamarillo+string+end
	elif color == 'bazul':
		return bazul+string+end
	elif color == 'brojo':
		return brojo+string+end
	elif color == 'bmagenta':
		return bmagenta+string+end
def style(style, string):
	
	if style == 'bold':
		return negrita+string+end
	elif style == 'underline':
		return subrallado+string+end
	elif style == 'reverse':
		return reverse+string+end	


def help():
	os.system('clear')
	return """
	---- Modulo para dar formato a la salida estandar ----

	Dar formato a las letras con los colores siguientes:

	magenta		--> Color magenta
	azul	 	--> Color azul
	verde		--> Color verde
	amarillo	--> Color amaraillo
	rojo		--> Color rojo
	cyan		--> Color cyan
	blanco		--> Color blanco
	negro 		--> Color negro

	Dar formato a los fondos de las letras con los colores siguientes:

	bmagenta	--> Color magenta
	bazul	 	--> Color azul
	bverde		--> Color verde
	bamarillo	--> Color amaraillo
	brojo		--> Color rojo
	bcyan		--> Color cyan
	bblanco		--> Color blanco
	bnegro 		--> Color negro

	Para su uso importarlo: import colores

						""" + negrita + """By Interhack""" + end



