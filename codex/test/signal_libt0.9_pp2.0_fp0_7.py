import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import gi
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk, GLib, WebKit2

from modules.pages.page_explorer import PageExplorer
from modules.pages.page_web import PageWeb
from modules.pages.page_hint import PageHint
from modules.pages.page_hints import PageHints

from modules.utils import get_default_browser, get_nice_size, get_content_type
from modules.bookmarks import Bookmarks

class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="id.archman.PythonBrowser",
                         flags=Gio.ApplicationFlags.HANDLES_COMMAND_LINE,
                         **kwargs)
        self.window = None
        self.builder = Gtk.Builder()
        self.builder.add_from_file('ui.glade')
