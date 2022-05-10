import types
types.ModuleType.__dict__['__file__'] = '<stdin>'

import sys
sys.path.append('/home/pi/Desktop/Code/Python/')

import time
import datetime
import os
import RPi.GPIO as GPIO
import Adafruit_DHT
import Adafruit_BMP.BMP085 as BMP085
import Adafruit_ADS1x15
import Adafruit_CharLCD as LCD
import Adafruit_GPIO.MCP230xx as MCP
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import Adafruit_MCP4725
import Adafruit_PCA9685
import Adafruit_PN532 as PN532
import Adafruit_TMP.TMP006 as TMP006
import Adafruit_TSL2561
import Adafruit_VCNL4000
import Adafruit_VL53L0X
import Adafruit_WS2801
import Adafruit_WS2811
import Adafruit_MAX31855.
