import signal
signal.signal(signal.SIGINT, signal_handler)

# Initialize the GPIO Pins
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

# Setup LED pins as outputs
GPIO.setup(LEDS, GPIO.OUT)

# Setup the PWM for each LED
RED = GPIO.PWM(RED_PIN, 100) # Channel, Frequency
GREEN = GPIO.PWM(GREEN_PIN, 100)
BLUE = GPIO.PWM(BLUE_PIN, 100)

# Initial duty cycle of 0 (LEDs off)
RED.start(0)
GREEN.start(0)
BLUE.start(0)

# Read the config file
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Get the WiFi SSID and Password
SSID = config.get('WIFI', 'ssid')
PASSWORD = config.get('WIFI', 'password')

# Connect to WiFi
station = network.WLAN(network.STA_IF)
station.active(True)

