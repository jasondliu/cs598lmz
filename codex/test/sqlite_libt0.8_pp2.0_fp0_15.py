import ctypes
import ctypes.util
import threading
import sqlite3

# this is necessary to make gi.require_version work
gi.require_foreign("cairo")
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Pango
from gi.repository import PangoCairo
from gi.repository import GtkSource
from gi.repository import Gio
from gi.repository import GdkPixbuf
from gi.repository import Notify
from gi.repository import WebKit

from time import time
from fnmatch import fnmatch
from gettext import gettext as _
from datetime import datetime
from hashlib import md5
from operator import attrgetter

from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.graphics.toolbutton import ToolButton
from sugar3.activity.widgets import ActivityToolbarButton
