import types
types.ModuleType.__repr__ = lambda self: '<module %r>' % self.__name__

# gtk
import pygtk
pygtk.require('2.0')
import gtk

# gtkmvc
import gtkmvc

# gtkmvc.adapters.basic
from gtkmvc.adapters.basic import BasicAdapter

# gtkmvc.adapters.liststore
from gtkmvc.adapters.liststore import ListStoreAdapter

# gtkmvc.adapters.treeview
from gtkmvc.adapters.treeview import TreeViewAdapter

# gtkmvc.adapters.scrolling
from gtkmvc.adapters.scrolling import ScrolledWindowAdapter

# gtkmvc.adapters.toggle
from gtkmvc.adapters.toggle import ToggleAdapter

# gtkmvc.adapters.combo
from gtkmvc.adapters.combo import ComboAdapter

# gtkmvc.adapters.spin
from gtkmvc.adapters.spin import Spin
