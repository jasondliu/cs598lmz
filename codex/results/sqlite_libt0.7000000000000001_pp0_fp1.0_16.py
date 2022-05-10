import ctypes
import ctypes.util
import threading
import sqlite3
import time

from gi.repository import Gdk
from gi.repository import Gtk
from gi.repository import GObject
from gi.repository import GdkPixbuf
from gi.repository import GLib
from gi.repository import Gio

import cairo

from ubuntutweak import system
from ubuntutweak.common.consts import DATA_DIR
from ubuntutweak.common.debug import run_traceback
from ubuntutweak.common.factory import Factory
from ubuntutweak.common.utils import*
from ubuntutweak.modules  import TweakModule
from ubuntutweak.widgets.dialogs import ErrorDialog
from ubuntutweak.utils import set_label_for_stock_button
from ubuntutweak.widgets.dialogs import InfoDialog
from ubuntutweak.policykit.dbusproxy import proxy

class UserGroupsDialog(object):
    def __init__(self, username, group_list):
        self.username = username
        self.group
