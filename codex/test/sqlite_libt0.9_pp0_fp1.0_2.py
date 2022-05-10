import ctypes
import ctypes.util
import threading
import sqlite3 as db
import time
import rtmidi

# midi device names
keyboard_name = 'LinnStrument'
guitar_name = 'A-49'

# sqlite database name
database_name = 'notes.sqlite'

# pi switch mode gpio pin
pi_switch_pin = 24

# input method class
class InputMethodClass:
	# name of the class
	name = "undefined"

	# class function that returns input string to be entered
	def getInput(self):
		return ""

# keyboard input class
class KeyboardInputClass(InputMethodClass):
	# name of the class
	name = 'kbrd'

	# class function that returns input string to be entered
	def getInput(self):
		return input()

# midi input class
class MidiInputClass(InputMethodClass):
	# name of the class
	name = 'midi'

	# class function that returns input string to be entered
	def getInput(self):
		message = self.midi_in.get_message
