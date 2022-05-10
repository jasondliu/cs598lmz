import threading
threading.stack_size(67108864)

from datetime import datetime
import sys
import time
import os
import uuid
import logging
import socket
import json

from azure.iot.device import IoTHubDeviceClient, Message
from azure.iot.device.provisioning.security.x509 import X509Security

import pytz
import RPi.GPIO as GPIO
from datetime import datetime
import paho.mqtt.client as mqtt
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import RPi.GPIO as GPIO
import time
import json

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(22,GPIO.OUT)
#pwm = GPIO.PWM(22,50)
#pwm.start(0)

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(33,GPIO.OUT)
# pwm2 = GPIO.PWM(33,50)
# pwm2.start(0)

