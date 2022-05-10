import gc, weakref, threading
import gtk, gtk.gdk
import gobject
from adesk.plugin import *
from adhoc import HidableVBox, gsignal, gui


header = ['#Name', 'Supplier', 'Price', 'Description']
stock = {'#0': 'Philly Cheesesteak', '#1': 'Apple Pie', '#2': 'McDonalds'}

menu_items = [
        ('Update...', lambda e,self: self.update_it()),
        ('Insert...', lambda e,self: self.insert_it()),
        ('Delete', lambda e,self: self.delete_it()),
        ]


class  ListModel(gtk.GenericTreeModel):
    def __init__(self, data):
        super(ListModel,self).__init__()
        self.data = data

    def on_get_flags(self):
        return gtk.TREE_MODEL_LIST_ONLY

    def on_get_n_columns(self):
        return 4

    def on_get_column
