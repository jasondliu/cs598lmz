import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

from .device import Device
from .tagger import Tagger
from pistream import __version__


PIXMAPS_DIR = path.join(path.abspath(path.dirname(__file__)), '../icons')

COLUMN_PIXBUF = 0
COLUMN_TEXT = 1
COLUMN_DEVICE = 2


class PiStream(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='org.pitheme.PiStream',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

        self.devices = {}
        self.tagger = Tagger()

        self.icon = path.join(PIXMAPS_DIR, 'pi-stream.png')
        gtk.window_set_default_icon_from_file(self.icon
