import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import pygtk
pygtk.require('2.0')
import gtk

import dbus
import dbus.service
import dbus.mainloop.glib

import gobject

from accessory import Accessory
from acc_config import *
from acc_window import *

class Manager(dbus.service.Object):

    def __init__(self, bus, loop):
        self.loop = loop
        self.path = '/'
        dbus.service.Object.__init__(self, bus, self.path)
        self.accessories = []

        self.window = acc_window()
        self.window.connect("delete-event", self.on_destroy)

        self.window.btn_add.connect("clicked", self.on_btn_add)
        self.window.btn_del.connect("clicked", self.on_btn_del)

        self.window.treeview.connect("cursor-changed", self.on_row_selected)


