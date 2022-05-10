import gc, weakref
from collections import namedtuple

from gi.repository import GObject, Gtk, Gdk, Gio

from kupfer import utils, icons, uiutils
from kupfer import pretty
from kupfer.ui import keybindings, idle_signal
from kupfer.ui import preferences
from kupfer.ui import browser, quickopen
from kupfer.ui import launch
from kupfer.ui import search
from kupfer.ui import keymap
from kupfer.ui import preferences as uiprefs
from kupfer.ui import plugin_preference
from kupfer.ui import widgets
from kupfer import kupferui
from kupfer import task
from kupfer import version
from kupfer import pretty
from kupfer import kupferstring
from kupfer import commandexec

from kupfer.ui import stats
from kupfer.ui.stats import Stats

from kupfer import pretty


_window = None
_window_id = 0
_window_id_lock = threading.Lock()

