#!/usr/bin/python
import Adafruit_BMP.BMP280 as BMP280
import requests
import pip._vendor.requests
import time
import json
#data = json.loads(urlopen('http://192.168.2.109/daten.json').read())
#import myopenfile
with open('/home/pi/Documents/daten.json') as f:
  data = json.load(f)
#data = {}
print(data)
sensor = BMP280.BMP280(address=0x76)
localtime = time.asctime( time.localtime(time.time()) )

temperature = sensor.read_temperature()
pressure = sensor.read_pressure()
#humidity = sensor.read_humidity()

print "Temperature : ", temperature, "C"
print "Pressure : ", pressure/100, "hPa"
#print "Humidity : ", humidity, "%"

f = open("Data.txt", "a")
f.write("\n" + str(localtime) + ", temp: " + str(temperature) + ", Druck: " + str(pressure))
f.close()

#data['people'] = []
data.append({
    'time': localtime,
    'temp': temperature,
    'druck': pressure
})
with open('/home/pi/Documents/daten.json', 'w') as outfile:
    json.dump(data, outfile)

