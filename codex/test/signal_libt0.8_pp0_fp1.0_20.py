import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from gi.repository import Gtk, Gdk, GObject

from src.Config import Config
from src.project_path import get_project_path
from src.MainWindow import MainWindow
from src.Clipboard import Clipboard
from src.AppMenu import AppMenu
from src.FileChooser import FileChooser
from src.Notification import Notification


class Application(GObject.GObject, Gtk.Application):
    def __init__(self):
        super(Application, self).__init__(application_id="de.freese.deepltranslator")

        self._clipboard = Clipboard()

        self._widget_style_provider = Gtk.CssProvider()
        self._widget_style_provider.load_from_path(os.path.join(get_project_path(), "res", "style.css"))

        self._notification = Notification()

        self._main_window = None

