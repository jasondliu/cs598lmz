import socket
import json
import datetime
import time
import paho.mqtt.client as mqtt
import random
import requests
import os

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

#==============================================
# MQTT Config
#==============================================
mqtt_broker_address = "192.168.2.30"
mqtt_client = mqtt.Client()
topic = "sensors/temp/sensor1"

#==============================================
# Read the temp
#==============================================
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines
