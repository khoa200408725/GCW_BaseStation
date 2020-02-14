#modified version 070220
import smbus2
import bme280
import time
import sys
import urllib.request
import json
import requests

from time import sleep

baseURLts = 'https://gcweather.azurewebsites.net/api/temperatures'
baseURLhs = 'https://gcweather.azurewebsites.net/api/humidities'
baseURLps = 'https://gcweather.azurewebsites.net/api/pressures'

port = 1

#I2C address is 76
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

# the compensated_reading class has the following attributes

while True:

    # the sample method will take a single reading and return a
    # compensated_reading object
    data = bme280.sample(bus, address, calibration_params)
    
    T = data.temperature
    P = data.pressure
    H = data.humidity

    dataT = {
            "value":T
            }
    
    dataP = {
            "value":P
            }
   
    dataH = {
            "value":H
            }
    
    reqT = requests.post(url = baseURLts, json = dataT)
    print("url:" + reqT.text)
    reqT.close()

    reqP = requests.post(url = baseURLps, json = dataP)
    print("url:" + reqP.text)
    reqP.close()
    
    reqH = requests.post(url = baseURLhs, json = dataH)
    print("url:" + reqH.text)    
    reqH.close()

    sleep(5)
    print("Ok")
    
print("--------")
