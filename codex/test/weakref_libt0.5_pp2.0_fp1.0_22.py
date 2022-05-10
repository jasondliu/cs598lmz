import weakref

from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GObject
from gi.repository import GdkPixbuf
from gi.repository import Pango

from gettext import gettext as _

from sugar3.graphics import style
from sugar3.graphics.palette import Palette
from sugar3.graphics.palettemenu import PaletteMenuBox
from sugar3.graphics.palettemenu import PaletteMenuItem
from sugar3.graphics.palettemenu import PaletteMenuItemSeparator
from sugar3.graphics.tray import TrayButton
from sugar3.graphics.icon import Icon
from sugar3 import profile
from sugar3.graphics.xocolor import XoColor

from jarabe.journal import misc
from jarabe.model import bundleregistry
from jarabe.journal.objectchooser import ObjectChooser
from jarabe.journal import model
from jarabe.journal import journalwindow
from jarabe.journal.detailview import DetailView
