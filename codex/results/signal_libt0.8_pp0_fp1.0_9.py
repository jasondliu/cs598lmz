import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from gi.repository import Gio
from gi.repository import GLib

from SCRIBES.SignalConnectionManager import SignalManager

class Handler(SignalManager):

	def __init__(self, manager, editor):
		SignalManager.__init__(self)
		self.__init_attributes(manager, editor)
		self.connect(manager, "destroy", self.__destroy_cb)
		self.connect(manager, "show-preferences-dialog", self.__show_cb)

	def __init_attributes(self, manager, editor):
		self.__manager = manager
		self.__editor = editor
		return

	def __destroy(self):
		self.disconnect()
		del self
		return

	def __show(self):
		try:
			self.__editor.show_preferences_dialog()
		except AttributeError:
	
