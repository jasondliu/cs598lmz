import weakref
import os
import sys
import os.path
import logging

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GObject, Pango, GLib, GdkPixbuf, Gio

import wayround_i2p.utils.path
import wayround_i2p.utils.gtk


class Base:

    def __init__(self):
        self._destroyed = False
        return

    def destroy(self):
        if not self._destroyed:
            self._destroy()
            self._destroyed = True
        return

    def _destroy(self):
        raise Exception("Not Implemented")
        return


class ScrollWin(Gtk.ScrolledWindow):

    def __init__(self, *args, **kwargs):
        Gtk.ScrolledWindow.__init__(self, *args, **kwargs)
        return


class TextView(Gtk.TextView):

    def __init__(self, *args, **kwargs):
       
