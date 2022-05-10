import weakref

from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GdkX11
from gi.repository import GObject
from gi.repository import WebKit
from gi.repository import GLib
from gi.repository import Pango
from gi.repository import PangoCairo
from gi.repository import GConf

from sugar3.graphics import style
from sugar3.graphics import animation
from sugar3.graphics.xocolor import XoColor
from sugar3.graphics.palette import Palette
from sugar3.graphics.icon import Icon
from sugar3.graphics.toggletoolbutton import ToggleToolButton
from sugar3.graphics.toolbutton import ToolButton

from jarabe.model import bundleregistry
from jarabe.model import shell
from jarabe.view.zoom import ZoomWidget
from jarabe.util.normalize import normalize_string

from browser import Browser
from bookmarks import Bookmarks
from home import Home
