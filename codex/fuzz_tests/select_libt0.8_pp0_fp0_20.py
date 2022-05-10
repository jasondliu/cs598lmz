import select
import sys
import time
import sched

# Version
VERSION = '1.0.0'

# Quit message
QUIT_MESSAGE = '\nQuitting...'

# Serial Port Variables
PORT_NAME = '/dev/tty.usbserial-A700eFyO'
BAUD_RATE = 9600
PARITY = 'N'
BYTESIZE = 8
STOPBITS = 1
SECONDS_TO_WAIT = 2

# Communication Protocol Variables
FRAME_LENGTH = 10
END_OF_FRAME_CHAR = ';'

# Message Variables
DECIMAL_PLACES = 2

# Operation mode variables
OPERATION_MODE_CHAR = 'O'
OPERATION_MODE = 'A'

# Backlight variables
BACKLIGHT_LED_CHAR = 'L'
BACKLIGHT_LED = '0'

# Contrast variables
CONTRAST_CHAR = 'C'
CONTRAST = '5'

# Data variables
TEMPERATURE_CHAR = 'T'
HUMIDITY
