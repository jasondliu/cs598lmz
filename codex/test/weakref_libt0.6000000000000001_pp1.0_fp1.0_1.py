import weakref

from gi.repository import Gtk, GObject

from .node import Node
from . import util
from . import model
from . import settings
from . import controller
from . import view


class Application(Gtk.Application):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id='com.github.gini.fresco',
                         flags=Gio.ApplicationFlags.HANDLES_OPEN,
                         **kwargs)
        self.window = None
        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        self.app_menu = Gio.Menu()
        self.app_menu.append('New', 'app.new')
        self.app_menu.append('Open', 'app.open')
        self.app_menu.append('Save', 'app.save')
