#Librerias
from Adafruit_IO import RequestError, Client, Feed
import serial, time
#Cuenta y llave de IO_Adafruit
ADAFRUIT_IO_USERNAME = 'Alejous'
ADAFRUIT_IO_KEY = 'aio_sQWz97iLvXSx54dsS9ZENKvhfeNN'
#Variable Global
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

while not False:
    #Leer puerto Serial y almacenarlo en una lista
    arduino = serial.Serial('COM5',9600)
    time.sleep(2)
    rawString = arduino.readline()
    lista_variables = rawString.decode().split(';')
    print(lista_variables[0])
    print(lista_variables[1])
    print(lista_variables[2])
    #Creación del Feed Humedad
    try:
        pyhum = aio.feeds('pyhum')

    except RequestError:
        pyhum_feed = Feed(name='pyhum')
        pyhum_feed = aio.create_feed(pyhum_feed)
    #Envio del dato Humedad a IO Adafruit    
    aio.send_data(pyhum.key, str(lista_variables[0]))
    #Creación del feed Temperatura
    try:
        pytemp = aio.feeds('pytemp')
          
    except RequestError:
        pytemp_feed = Feed(name='pytemp')
        pytemp_feed = aio.create_feed(pytemp_feed)
    #Envio el dato Temperatura a IO Adafruit             
    aio.send_data(pytemp.key, str(lista_variables[1]))
    #Cierro el Puerto Serial      
    arduino.close ()
