# Adafruit_IO-python-Arduino
En este repositorio encontraras un código que te permitirá acceder a los datos enviados desde arduino o cualquier otro equipo por un puerto serial, y serán cargados a la plataforma IO.Adafruit
Para que el codigo funcione sin ningun problema, solo es necesario instalar las librerias de io.adafruit, Serial, y time de la siguiente manera  (Para windows 10):
1- Abra una consola de comandos (Simbolo del Sistema)
2-escriba: python -m  pip  install  adafruit-io
3- libreria Serial: python -m pip install serial
En los archivos cargados en este repositorio se encuentra un ejemplo de datos de humedad y temperatura (DHT11) enviados desde arduino mega y leidos desde python para ser cargados en la plataforma de Adafruit para Iot, tambien se encuentra un feed adicional para la manipulacion de una salida digital y creo que por el lado de la programacion en python no tiene problema, pero si al recibir la info por serial desde arduino, agradezco contribuciones.
