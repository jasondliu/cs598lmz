import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from .core import main
from . import ui


def run_ui():
    main(ui.MainWindow())
    Gtk.main()
