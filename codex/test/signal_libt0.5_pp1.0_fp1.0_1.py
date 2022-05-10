import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from gi.repository import Gtk

from . import misc
from . import settings
from . import ui
from . import util
from . import windows


class MainWindow(windows.MainWindow):
    """
    Main application window.

    This is the window that is initially shown when the application is started.
    """

    def __init__(self, app):
        super().__init__()

        self._app = app

        self.set_title(settings.APP_NAME)
        self.set_default_size(settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_icon_name(settings.APP_ICON)

        self._headerbar = Gtk.HeaderBar()
        self._headerbar.set_show_close_button(True)
        self._headerbar.set_title(settings.APP_NAME)
