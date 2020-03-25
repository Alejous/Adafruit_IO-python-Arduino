#Librerias
from Adafruit_IO import RequestError, Client, Feed
import serial, time
#Cuenta y llave de IO_Adafruit
ADAFRUIT_IO_USERNAME = 'Alejous'
ADAFRUIT_IO_KEY = 'xxxxxxxxxxxxxxx'
#Variable Global
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
#Creación del Feed Humedad
try:
    pyhum = aio.feeds('pyhum')

except RequestError:
    pyhum_feed = Feed(name='pyhum')
    pyhum_feed = aio.create_feed(pyhum_feed)
#Creación del feed Temperatura
try:
    pytemp = aio.feeds('pytemp')
          
except RequestError:
    pytemp_feed = Feed(name='pytemp')
    pytemp_feed = aio.create_feed(pytemp_feed)
#Creacion del feed digital
try: # if we have a 'digital' feed
    digital = aio.feeds('digital')
except RequestError: # create a digital feed
    feed = Feed(name="digital")
    digital = aio.create_feed(feed)
    
    
    
while not False:
    #Leer puerto Serial y almacenarlo en una lista
    arduino = serial.Serial('COM5',9600)
    time.sleep(2)
    rawString = arduino.readline()
    lista_variables = rawString.decode().split(';')
    data = aio.receive(digital.key)
    if int(data.value) == 1:
        print('received <- ON')
        arduino.write(int(data.value))
    elif int(data.value) == 0:
        print('received <- OFF')
        arduino.write(int(data.value))
        
    lista_variables[0] = float(lista_variables[0])
    lista_variables[1] = float(lista_variables[1])
    lista_variables[2] = float(lista_variables[2])
    print('Humidity={0:0.1f}% Temp={1:0.1f}°C Temp={2:0.1f}°F'.format(lista_variables[0], lista_variables[1], lista_variables[2]))
        
    #Envio del dato Humedad a IO Adafruit    
    aio.send_data(pyhum.key, str(lista_variables[0]))
    
    #Envio el dato Temperatura a IO Adafruit             
    aio.send_data(pytemp.key, str(lista_variables[1]))
    #Cierro el Puerto Serial      
    arduino.close ()
