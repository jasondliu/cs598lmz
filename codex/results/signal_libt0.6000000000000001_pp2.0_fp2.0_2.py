import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk

import re

from widgets.color_picker import ColorPicker
from widgets.color_picker import ColorPickerEntry
from widgets.color_picker import ColorPickerButton

from widgets.color_picker import ColorPickerButton

class TestWindow(gtk.Window):

    def __init__(self):
        gtk.Window.__init__(self, title="Color Picker Test")
        self.set_default_size(800, 600)

        self.connect("destroy", gtk.main_quit)

        box = gtk.Box(orientation=gtk.Orientation.VERTICAL)
        self.add(box)

        box.pack_start(ColorPickerButton(), False, False, 0)
        box.pack_start(ColorPicker(), False, False, 0)

        color_picker_entry =
