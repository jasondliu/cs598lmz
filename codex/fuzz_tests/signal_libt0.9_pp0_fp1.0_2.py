import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from gi.repository import Gtk, Gdk

from .mainwindow import MainWindow
from .app import App


def run():
    """Run the app"""
    App()
    Gtk.main()


def run_async(cb_start=None, cb_stop=None):
    """Run the app in a separate thread

    Allows the application to run in a thread.

    For instance, to prevent your main thread from freezing
    while the main window is loading.

    Args:
        cb_start(Callable, optional): Callback execute in the main application
            thread when the run loop is started. Called with (app, main_window)
        cb_stop(Callable, optional): Callback to execute in the application
            thread when the run loop exit. Called with (app, main_window)

    Typically, cb_start is used for loading data and cb_stop for saving it,
    but you can use them for anything you want. They are good ways to

