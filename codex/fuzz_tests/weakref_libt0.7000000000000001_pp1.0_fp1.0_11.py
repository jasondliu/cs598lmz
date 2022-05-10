import weakref

from gi.repository import Gdk, Gio, GLib, GObject, Gtk, Vte

from lutris.runners.runner import Runner
from lutris.thread import LutrisThread
from lutris.util import datapath, system
from lutris.util.log import logger
from lutris.util.strings import decode
from lutris.util.system import path_exists
from lutris.util.threading import ThreadedTask

DEFAULT_TERMINAL = "xterm"
DEFAULT_TERMINALS = ["gnome-terminal", "xfce4-terminal", "konsole", DEFAULT_TERMINAL]
TERMINAL_MAPPING = {
    "gnome-terminal": "gnome-terminal --hide-menubar",
    "xfce4-terminal": "xfce4-terminal --hide-menubar",
    "konsole": "konsole --hide-menu",
    "xterm": "xterm"
}


class TerminalBox(Gtk
