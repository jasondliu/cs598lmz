import weakref
import os
import os.path
import tempfile
import shutil

import gtk
import gtk.gdk
import gtk.glade

from caja import ui_manager
import caja

from caja.ui_manager import ui_reference_new
from caja.extensions import CajaExtension, WindowActivatable

from caja.propertiespage import PropertiesPageProvider
from caja.columns import TextColumn, DateColumn, RatingColumn

from caja import compat
import caja.actions

from caja.bookmarks import bookmark_exists, bookmark_get_by_uri, bookmark_list_model_new, \
    get_bookmarks_menu, get_places_menu, get_desktop_dir

from caja.lru_cache import lru_cache

from caja.settings import CajaSettings

from caja.signal import signal_connect_after, signal_connect_object_after, signal_connect_object, signal_connect

from caja.debug import debug
from caja.util import file_manager_uri_is_
