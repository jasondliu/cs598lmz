import gc, weakref, os, sys, shutil, time
import gtk, gtk.gdk, gobject
import gtk.glade
import pango, pangocairo

import cairo, rsvg

import logging
log = logging.getLogger("core.svgtheme")

import gs
import gs.ui
import gs.icons
import gs.config
import gs.ui.theme

import themes

from widgets.decorators import DBUS_Call, DBUS_Signal

from decorators import *

#-------------------------------------------------------------------------

theme_directories = [
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "themes")),
    os.path.abspath(os.path.join(os.path.expanduser("~"), ".gnome-schedule", "themes")),
    "/usr/share/gnome-schedule/themes",
    "/usr/local/share/gnome-schedule/themes"
]

g_tile 
