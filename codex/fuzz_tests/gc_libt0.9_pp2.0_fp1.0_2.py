import gc, weakref
import bisect
import time
import threading
import __main__
import traceback
import pygame.event
import pygame.locals

_next_sequence = 100000
_next_thread_sequence = 1000
_thread_weakdict = weakref.WeakKeyDictionary()


def _sequence():
	global _next_sequence
	_next_sequence += 1
	return _next_sequence

#
# Event
#


class Event:
	"""Event(type, **kwargs)
	Called by pygame internally to pass events to user code.
	Events are accessible from the pygame.event.get() function.
	All events are placed into the queue automatically by pygame.
	All attributes are read only.
	"""
	__slots__ = (
		'_type',
		'_dict',
		)

	def __init__(self, type, **kwargs):
		self._type = type
		self._dict = kwargs  # we have to have a dict because dicts can be weak referenced

	def __repr__
