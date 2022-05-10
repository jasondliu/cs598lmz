import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os.path
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

from lib.config import get_data_path, get_ui_path
from lib.refresh_thread import RefreshThread


class TrayIcon(Gtk.StatusIcon):

    def __init__(self):
        Gtk.StatusIcon.__init__(self)
        self.set_from_file(os.path.join(get_data_path(), "images",
                                        "tray-icon.png"))
        self.set_tooltip_text("RSS Tray")
        self.set_visible(True)

        self.menu = Gtk.Menu()
        self.menu_item_quit = Gtk.MenuItem("Quit")
        self.menu_item_quit.connect("activate", self.quit)
        self.menu.append(self.menu_item_quit)

        self.menu
