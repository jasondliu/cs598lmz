import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from gi.repository import Gdk

from .builder import Builder
from .window import Window
from .application import Application
from .utils import (
    get_icon_pixbuf,
    get_application,
    Color,
)

if Gtk.get_minor_version() >= 20:
    from .scalebutton import ScaleButton
    from .spinbutton import SpinButton
    from .entry import Entry
    from .combobox import ComboBox
    from .comboboxentry import ComboBoxEntry
    from .switch import Switch
    from .levelbar import LevelBar
    from .textview import TextView
    from .textbuffer import TextBuffer
    from .texttag import TextTag
    from .texttagtable import TextTagTable
    from .iconview import IconView
    from .treeview import TreeView
    from .drawingarea import DrawingArea

