import ctypes
import ctypes.util
import threading
import sqlite3
import time

from struct import unpack

from gi.repository import Gtk, Gdk, GObject

from pyanaconda.anaconda_loggers import get_module_logger
from pyanaconda.core.i18n import _
from pyanaconda.core.constants import THREAD_LIVE_PROGRESS
from pyanaconda.core.util import join_paths
from pyanaconda.modules.common.constants.objects import PAYLOAD
from pyanaconda.ui.communication import hubQ
from pyanaconda.ui.gui import GUIObject
from pyanaconda.ui.gui.spokes import NormalSpoke
from pyanaconda.ui.categories.software import SoftwareCategory
from pyanaconda.ui.gui.utils import gtk_call_once, ignoreEscape, escape_markup
from pyanaconda.ui.gui.utils import setViewportBackground, setViewportOverlay
from pyanaconda.ui.gui.spokes.lib.detailederror import DetailedErrorDialog
from pyan
