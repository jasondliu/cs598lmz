import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from . import settings
from . import ui
from . import utils
from . import updater
from . import version
from . import webview
from . import window
from . import zoom


class Application(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self,
                                 application_id='org.gnome.Epiphany',
                                 flags=Gio.ApplicationFlags.HANDLES_COMMAND_LINE)

        self.add_main_option('new-tab', ord('t'), GLib.OptionFlags.NONE,
                             GLib.OptionArg.NONE, _("Open a new tab"), None)
        self.add_main_option('new-window', ord('n'), GLib.OptionFlags.NONE,
                             GLib.OptionArg.NONE, _("Open a new
