import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from gi.repository import Gtk, Gdk

from .mainwindow import MainWindow
from .app import App


def run():
    """Run the app"""
    App()
    Gtk.main()


