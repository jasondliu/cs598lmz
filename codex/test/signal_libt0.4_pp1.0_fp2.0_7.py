import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from . import settings
from . import utils
from . import keybindings
from . import preferences
from . import shortcuts
from . import appmenu
from . import statusicon
from . import window
from . import tray
from . import log
from . import updater
from . import pluginmanager

from .i18n import _
from .const import APP_ID, APP_NAME, APP_VERSION, APP_URL, APP_COPYRIGHT, APP_AUTHOR, APP_ICON_NAME
from .const import CONFIG_DIR, CONFIG_PATH, DATA_DIR, PLUGINS_DIR, PLUGINS_DATA_DIR, PLUGINS_SETTINGS_DIR
from .const import PLUGINS_ENABLED_FILE, PLUGINS_DISABLED_FILE, PLUGINS_INSTALLED_FILE, PLUGINS_INFO_FILE
