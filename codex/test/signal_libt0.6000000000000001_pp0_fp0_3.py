import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from gi.repository import Gtk, Gdk, GLib, GObject

from . import log, config, ui, core, httpd, frontends
from .gtk_frontend.main_window import MainWindow
from .gtk_frontend.preferences import PreferencesDialog
from .gtk_frontend.subscriptions import SubscriptionsDialog
from .gtk_frontend.about import AboutDialog
from .gtk_frontend.player import PlayerDialog
from .gtk_frontend.add_dialog import AddDialog
from .gtk_frontend.playlist_manager import PlaylistManager
from .gtk_frontend.playlist_dialog import PlaylistDialog
from .gtk_frontend.playlist_dialog import PlaylistItem
from .gtk_frontend.find_dialog import FindDialog
from .gtk_frontend.pafy import PafyDialog
from .gtk_frontend.downloads import DownloadsDialog
