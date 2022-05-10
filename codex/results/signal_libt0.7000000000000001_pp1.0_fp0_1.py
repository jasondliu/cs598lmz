import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from gi.repository import Gtk, Gdk, GdkPixbuf, GObject
import os, sys

try:
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
    from src.gnome import Gnome
except ImportError, e:
    print "Couldn't find gnome.py:", e
    sys.exit(1)

class Window(Gtk.Window):
    __gtype_name__ = "Window"

    def __init__(self):
        super(Window, self).__init__()
        try:
            self.set_screen(Gdk.Screen.get_default())
        except:
            self.connect('destroy', lambda *w: Gtk.main_quit())
        self.set_title(__file__)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_default_size(450,
