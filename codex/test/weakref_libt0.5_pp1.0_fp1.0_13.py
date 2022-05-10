import weakref

from . import gi
from . import _gobject

Gtk = gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gdk, GObject, GLib

from .util import idle
from . import util

from . import keymap
from . import keybindings
from . import config
from . import options
from . import commands
from . import command_dispatcher
from . import qtile
from . import hook
from . import window
from . import layout
from . import bar
from . import widget
from . import xcbq
from . import xcffib
from . import xcffib_xproto
from . import command
from . import xcb
from . import xcursor
from . import xinerama
from . import xkb
from . import xrandr
from . import xutils
from . import xwindow
