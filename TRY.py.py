import smbus2
import bme280
import time
import sys
import urllib.request

from time import sleep

baseURLts = 'http://api.thingspeak.com/update?api_key=N1QMGULPCJJDWBSD&field1='
baseURLhs = 'https://api.thingspeak.com/update?api_key=MUQTNJQ9BMSPUYSC&field1='
baseURLps = 'https://api.thingspeak.com/update?api_key=RY2YP6AK8LIG2O6U&field1='

port = 1

#I2C address is 76
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

# the sample method will take a single reading and return a
# compensated_reading object
data = bme280.sample(bus, address, calibration_params)

# the compensated_reading class has the following attributes

while True:
    
    T = data.temperature
    P = data.pressure
    H = data.humidity
   
    TS = urllib.request.urlopen(baseURLts + str(T))
    TS.read()
    TS.close()

    HS = urllib.request.urlopen(baseURLhs + str(H))
    HS.read()
    HS.close()

    PS = urllib.request.urlopen(baseURLps + str(P))
    PS.read()
    PS.close()

    
    sleep(5)
    print("Ok")
print("--------")
