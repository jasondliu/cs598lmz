import weakref

import gio
import glib

from pygi.repository import Gdk, Gtk, GObject
from pygi.repository.GdkPixbuf import Pixbuf
from pygi.repository.Gio import Settings
from pygi.repository.GObject import TYPE_NONE, TYPE_BOOLEAN, TYPE_STRING, TYPE_UINT

from gui import gui
from gui.widgets import ExtractionDialog, ButtonSettings
from gui.pluginloader import PluginLoader
from gui.clip import Clip
from gui.clipboard import Clipboard
from gui.config import Config
from gui.extractor import Extractor
from gui.extractor import SUPPORTED_FORMATS
from gui.events import manager
from actions.main_window import MainWindowActions
from actions.preferences import PreferencesActions
from actions.extractor_dialog import ExtractorActions
from actions.button_settings_dialog import ButtonSettingsDialogActions

from extractors.imgur import ImgurExtractor
from extractors.imgur_album import ImgurAlbumExtractor

from zim
