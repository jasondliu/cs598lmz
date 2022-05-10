import select, serial, sys, termios, tty
from time import sleep

MODE_SINGLE_CHAR = 'c'
MODE_STRING = 's'
MODE_INT = 'i'

PRINT_AT_START = False
PRINT_AT_END = True
PRINT_MESSAGE_TO_SCREEN = False
PRINT_INPUT_TO_SCREEN = False
PRINT_AFTER_RESPONSE = False

# no default values, to make sure there's no confusion.
class SerialConfiguration:
	def __init__(self, baud_rate, port, message, mode=None): 
		self.baud_rate = baud_rate
		self.port = port
		self.message = message
		
		if mode is None:
			mode = ( MODE_SINGLE_CHAR )
		self.mode = mode
		
class SerialInput:
	def __init__(self, port, timeout = 0.1, min = 0.0, max = 0.0, default =
