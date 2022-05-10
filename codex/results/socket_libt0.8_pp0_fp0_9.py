import socket, threading
from time import sleep

from luma.core.interface.serial import i2c
#from luma.core.render import canvas
#from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
#from luma.core.legacy import text, show_message
#from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
#import sys

#D_SCL = 4
#D_SDA = 5

D_SCL = 5
D_SDA = 6

GPIO.setmode(GPIO.BCM)

#Boton de pausa/resume
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Leds de actividad, modem y estado del magnetometro
GPIO.setup(26, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21
