import mmap
import time
import sys, os
sys.path.append(os.path.expanduser('~/projects/rpi_gpio_lcd_kbd/py'))

from rpi_gpio_lcd.lcd_1602 import LCD1602
from rpi_gpio_lcd.joystick import Joystick
from rpi_gpio_lcd.keypad import Keypad

from rpi_gpio_lcd.tools import findDeviceNum

print('Press Joystick Button or push MENU to quit')
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
    
# create *only* needed objects
LCD_RS = 15
LCD_E = 13
LCD_D4 = 24
LCD_D5 = 22
LCD_D6 = 27
LCD_D7 = 17
LCD_COLS = 16
LCD_ROWS = 2

lcd = LCD1602(rs=LCD_RS,e=LCD_E,d4=LCD_D4,d
