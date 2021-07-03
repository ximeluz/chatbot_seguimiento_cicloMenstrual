# Contador de ciclo 28 dias.
####   formato dia/mes/año todo en numero 22 03 2021  ###

from datetime import datetime, timedelta

'''  Convertimos un string con formato <día>/<mes>/<año> en datetime

una_fecha = '20/04/2019'
fecha_dt = datetime.strptime(una_fecha, '%d/%m/%Y')
print(fecha_dt)
###> 2019-04-20 00:00:00
### Comprobación del tipo del objeto fecha_dt
###print(type(fecha_dt))
###<class 'datetime.datetime'>  '''


''' Funcion que convierte cadena a fecha con formato  dia mes año con:  "22 03 2021"  '''

def cadena_a_fecha(cadena):
	fecha = datetime.strptime(cadena, '%d %m %Y')
	
	return fecha

''' EJEMPLO:
Cadena = '22 03 2020'
fecha = cadena_a_fecha(Cadena)

print(type(fecha))
print(fecha)
FIN DE EJEMPLO '''

''' Contador de la fecha actual a la fecha 28 dias despues 

hoy = datetime.now()
print(hoy.strftime("%x"))
#day = int(input("Ingresa los días de tu periodo"))
fecha_futura = hoy + timedelta(days = 28)

print(fecha_futura.strftime("%x"))
'''
