import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# gi is a python library that enables us to use
# the GTK+3 toolkit to create our application
# more information at http://www.pygtk.org/
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# main window
class main_window(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Gtk.Entry")
		# init grid
		# self.set_border_width(5)
		# self.grid = Gtk.Grid()
		# self.grid.set_column_homogeneous(True)
		# self.grid.set_row_homogeneous(True)
		# self.add(self.grid)

		# create a combobox
		combobox = Gtk.ComboBoxText()
		combobox.append_text("C Programming")

