import signal
signal.signal(signal.SIGTERM, signal.SIG_DFL)

import sys,os
from gi.repository import Gtk, Gdk

from constants import *

class GtkUI:
	"""
	Main GUI class
	"""
	def __init__(self, app, config):
		self.app = app
		self.config = config
		self.builder = Gtk.Builder()
		self.builder.add_from_file(UI_FILE)
		self.builder.connect_signals(self)
		self.main_window = self.builder.get_object('main_window')
		self.main_window.show()

	def on_main_window_destroy(self, widget):
		"""
		Quit program
		"""
		self.config.save_config()
		Gtk.main_quit()

	def on_main_window_delete_event(self, widget, event):
		"""
		Quit program
		"""
		self
