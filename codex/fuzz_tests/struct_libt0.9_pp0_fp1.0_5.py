import _struct
from operator import itemgetter
from ctypes import *
from microchip import MCP23017
from pprint import pprint

class LCD2004(object):

  LCD_ADDR = 0x27
  LCD_CGRAM = 0x40
  LCD_DGRAM = 0x80
  LCD_BUSY = 0x80
  LCD_MAXCHAR = 20

  LCD_ENTRY_MODE = 0x04
  LCD_DISPLAY_ON_OFF = 0X08
  LCD_SHIFT = 0x10
  LCD_FUNC_SET = 0x20
  LCD_SET_CGRAM_ADDR = 0x40
  LCD_SET_DDRAM_ADDR = 0x80

  LCD_BIAS = 0x10
  LCD_FWIDTH = 0x20
  LCD_ONE_LINE = 0x00
  LCD_TWO_LINE = 0x08
  LCD_FONT = 0x04
  LCD_POWER = 0x04
  LCD_CONTRAST = 0x02
  LCD_FOLLOW = 0x01
  LCD
