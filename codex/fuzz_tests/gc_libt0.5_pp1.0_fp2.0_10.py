import gc, weakref

from gi.repository import Gtk, Gdk

from kiwi.ui.objectlist import ObjectList, Column
from kiwi.ui.gadgets import render_pixbuf
from kiwi.ui.delegates import SlaveDelegate
from kiwi.ui.widgets.list import Column as ListColumn
from kiwi.ui.widgets.combo import ProxyComboBox
from kiwi.ui.dialogs import warning, error
from kiwi.ui.dialogs import yesno
from kiwi.ui.widgets.checkbutton import ProxyCheckButton
from kiwi.ui.widgets.entry import ProxyEntry
from kiwi.ui.widgets.label import ProxyLabel
from kiwi.ui.widgets.spinbutton import ProxySpinButton
from kiwi.ui.widgets.textview import ProxyTextView
from kiwi.ui.widgets.button import ProxyButton
from kiwi.ui.widgets.search import SearchFilter
from kiwi.ui.editors import ComboEditor, DateEditor, DateTime
