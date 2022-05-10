import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/home/pi/Desktop/test.db')

# Global variables
# Set up the database
# conn = sqlite3.connect('/home/pi/Desktop/test.db')
# c = conn.cursor()
# c.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, time TEXT, temp REAL)")
# conn.commit()
# conn.close()

# Set up the sensor
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

# Set up the LED
led = LED(17)
led.on()

# Set up the button
button = Button(2)

# Set up the buzzer
buzzer = Buzzer(4)

# Set up the LCD
lcd = CharLCD()

