import threading
threading.stack_size(67108864)

#Import the Adafruit IO MQTT client.
from Adafruit_IO import MQTTClient

# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = 'f9796b7e0d864f3ba09a80a8a1b7f4a4'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'pranavjha91'


# Set to the ID of the feed to subscribe to for updates.
FEED_ID = 'switch'


# Define callback functions which will be called when certain events happen.
