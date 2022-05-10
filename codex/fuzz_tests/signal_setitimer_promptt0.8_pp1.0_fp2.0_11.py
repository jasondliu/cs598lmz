import signal
# Test signal.setitimer()
# This script registers a signal handler for SIGALRM, sets an interval timer
# for 10 seconds, then goes to sleep for 20 seconds.
# A SIGALRM should be delivered after 10 seconds, at which point it should toggle the LED

# Import standard python modules
import time
import sys

# Import Adafruit IO MQTT client.
import Adafruit_IO

# Import Adafruit IO HTTP client.
# import Adafruit_IO.HttpClient

# import Adafruit IO MQTT client.
from Adafruit_IO import MQTTClient

# import Adafruit IO REST client.
from Adafruit_IO.rest import Client

import busio

# Change to the correct value for your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY='f15814e0b0f94d4d949e0e6c53cdb766'
ADAFRUIT_IO_USERNAME='ian-fielding'
# Create
