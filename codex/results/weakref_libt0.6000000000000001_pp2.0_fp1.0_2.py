import weakref
import webbrowser

from gi.repository import GLib, GObject, Gtk, Gdk, Pango
from gi.repository import Gedit

import gettext

from . import config
from . import gtkutils
from . import utils


_ = gettext.gettext

class MessageWindow(Gedit.WindowActivatable):

    __gtype_name__ = 'MessageWindow'

    window = GObject.property(type=Gedit.Window)

    def __init__(self):
        GObject.Object.__init__(self)
        self.window_handlers = []
        self.view_handlers = []

    def do_activate(self):
        self.window_handlers.append(self.window.connect('tab-added', self.on_tab_added))
        self.window_handlers.append(self.window.connect('tab-removed', self.on_tab_removed))
        for view in self.window.get_views():
            self.connect_view(view)

    def connect_view(
