import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from . import config
from . import widgets


class App(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='com.github.qwertzguy.dockbarx',
                         flags=Gio.ApplicationFlags.HANDLES_COMMAND_LINE)

        self.add_main_option(
            "--disable-indicator",
            ord("i"),
            GLib.OptionFlags.NONE,
            GLib.OptionArg.NONE,
            "Disable the indicator",
            None
        )

        self.add_main_option(
            "--disable-tray",
            ord("t"),
            GLib.OptionFlags.NONE,
            GLib.OptionArg.NONE,
            "Disable the tray",
            None
        )

        self.add_main_
