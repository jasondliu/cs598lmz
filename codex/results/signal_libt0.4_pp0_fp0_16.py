import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from gi.repository import Gtk, Gdk

from . import settings
from . import utils
from . import widgets
from . import window
from . import pathbar
from . import prefs
from . import statusbar
from . import tabbar
from . import notebook
from . import filelist
from . import terminal
from . import dialogs
from . import fileops
from . import history
from . import bookmarks
from . import clipboard
from . import search
from . import ui
from . import keybindings
from . import commands
from . import app
from . import thunar
from . import plugin
from . import config

from . import __version__

# i18n
from gettext import gettext as _

#------------------------------------------------------------------------------

class MainWindow(window.Window):
    """
    Main application window.
    """
    def __init__(self):
        """
        Create a new MainWindow instance.
        """
        window.Window.__init__(self)
