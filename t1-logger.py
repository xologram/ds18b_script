#!/usr/bin/python3

from datetime import datetime
import os, time

from influxdb_client import WritePrecision, InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

token = "YOUR_TOKEN_GOES_HERE"
temp_sensor1 = '/sys/bus/w1/devices/28-3c01a8160b24/w1_slave'
org = "."
bucket = "home_temp"
host = "YOUR_HOSTNAME"

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

def temp_raw():
    f = open(temp_sensor1, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = temp_raw()
    temp_output = lines[1].find('t=')
    if temp_output != -1:
        temp_string = lines[1].strip()[temp_output+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

with InfluxDBClient(url="http://localhost:8086", token=token, org=org, debug=True) as client:
    while True:
        temperature = read_temp()
    
        p = Point("temp_sensor1_vessel_celcius").tag("host",host).field("value", temperature)
        write_api = client.write_api(write_options=SYNCHRONOUS)
        write_api.write(bucket=bucket, org=org, record=p)
    
        time.sleep(10)
