# Contador para fechas del periodo.
####   formato mes/dia/año  ###

from datetime import datetime, timedelta

'''  Convertimos un string con formato <día>/<mes>/<año> en datetime '''

una_fecha = '20/04/2019'
fecha_dt = datetime.strptime(una_fecha, '%d/%m/%Y')
print(fecha_dt)
#> 2019-04-20 00:00:00
# Comprobación del tipo del objeto fecha_dt
#print(type(fecha_dt))
#<class 'datetime.datetime'>


''' Funcion que convierte cadena a fecha con formato mes dia año con:  "feb 22 2021"  '''

def convertir_cadena_a_fecha(cadena):
	fecha = datetime.strptime(cadena, '%b %d %Y')
	
	return fecha

cadena_fecha = 'Feb 22 2020'
fecha = convertir_cadena_a_fecha(cadena_fecha)

print(type(fecha))
print(fecha)


''' Contador de la fecha actual a la fecha 28 dias despues '''

hoy = datetime.now()
print(hoy.strftime("%x"))
#day = int(input("Ingresa los días de tu periodo"))
fecha_futura = hoy + timedelta(days = 28)

print(fecha_futura.strftime("%x"))

