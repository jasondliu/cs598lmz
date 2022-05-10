import weakref
import sound_lib.sound as sound
import threading

# Sources:
# https://www.pygame.org/wiki/GettingStarted
# http://www.monkeysee.com/play/20266-how-to-create-a-command-line-calculator-in-python-part-2
# https://www.quora.com/How-do-I-map-a-number-from-one-number-range-to-another-1-5-to-5-10

VOLUME=.8

class TrumpeterPlayer(object):

	def __init__(self):
		from sound_lib.sound import Note

