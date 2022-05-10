import weakref

from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GObject
from gi.repository import Gio
from gi.repository import Pango

from kupfer.objects import Leaf
from kupfer import icons
from kupfer.objects import Source, Action, OperationError
from kupfer.objects import TextLeaf, FileLeaf, RunnableLeaf
from kupfer import utils
from kupfer import pretty
from kupfer import kupferstring
from kupfer import plugin_support
from kupfer.weaklib import WeakKeyDictionary
from kupfer import config
from kupfer import version
from kupfer import task

from kupfer.ui import keybindings
from kupfer.ui import preferences

from kupfer.ui.gtkui.uicompat import ui_util
from kupfer.ui.gtkui import icons as gtk_icons

from kupfer.ui.gtkui.uicompat import
