import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect fail
try:
	conn = sqlite3.connect("/home/rtrr/share_code/flask_test/tmb_test/office_word/word.db")
	conn.close()
	FLAG = True
except:
	FLAG = False
	pass

class Event:
	"""Base class for all event types."""
	def __init__(self, etype, **attrs):
		self.type = etype
		self.attrs = attrs

	def __getattr__(self, name):
		try:
			return self.attrs[name]
		except KeyError:
			raise AttributeError(name)

	def __repr__(self):
		return '%s(%s)' % (self.type, ', '.join(['%s=%r' % (k, v) for k, v in self.attrs.items()]))


class DocumentChangeEvent(Event):
	"""Emitted when the viewed document changes.

	Attributes:
	docx: Path to document
	
