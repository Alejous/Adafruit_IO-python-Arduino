#include "DHT.h"
#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);
char input;
void setup() {
pinMode(13 , OUTPUT);
Serial.begin(9600);
dht.begin();
input=0;
}

void loop() {
if (Serial.available()>0){
input=Serial.read();
if (input=='1'){
digitalWrite(13,HIGH);

}
else
{
digitalWrite(13, LOW); //Si el valor de input es diferente de 1, se apaga el LED

}
}
float h = dht.readHumidity();  
float t = dht.readTemperature();
float f = dht.readTemperature(true);
delay(9000);  
Serial.print(h);
Serial.print(";");
Serial.print(t);
Serial.print(";");
Serial.print(f);
Serial.println(";");
//Serial.println(input);

  
}
