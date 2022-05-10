import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from . import utils

class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="org.gnome.SettingsDaemon.Color",
                         flags=Gio.ApplicationFlags.HANDLES_COMMAND_LINE,
                         **kwargs)

        self.add_main_option("test", ord("t"), GLib.OptionFlags.NONE,
                             GLib.OptionArg.NONE, "Command line test mode", None)

        self.connect("command-line", self.on_command_line)

    def on_command_line(self, app, cmd):
        options = cmd.get_options_dict()
        if options.contains("test"):
            self.activate()
            return 0

        self.activate()
        self.
