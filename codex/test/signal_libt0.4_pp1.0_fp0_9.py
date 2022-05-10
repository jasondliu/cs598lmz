import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf

from . import utils
from . import settings
from . import config

from .widgets.window import MainWindow
from .widgets.dialogs import AboutDialog, PreferencesDialog
from .widgets.dialogs import AddBookmarkDialog, EditBookmarkDialog
from .widgets.dialogs import AddDownloadDialog
from .widgets.dialogs import AddTorrentDialog
from .widgets.dialogs import AddMagnetDialog
from .widgets.dialogs import AddRssDialog
from .widgets.dialogs import AddRssFeedDialog
from .widgets.dialogs import AddRssFilterDialog
from .widgets.dialogs import AddRssFilterRuleDialog
from .widgets.dialogs import AddRssFilterRuleActionDialog
from .widgets.dialogs import AddRssFilterRuleActionParameterDialog
