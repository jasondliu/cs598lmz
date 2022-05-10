import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys

from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GObject
from gi.repository import GdkPixbuf

from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.activity.widgets import StopButton
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.graphics.toolbutton import ToolButton
from sugar3.graphics.toggletoolbutton import ToggleToolButton
from sugar3.graphics.radiotoolbutton import RadioToolButton
from sugar3.graphics.icon import Icon
from sugar3.graphics.xocolor import XoColor
from sugar3.graphics import style

from gettext import gettext as _

import telepathy
import telepathy.client
from dbus.service import signal as dbus_signal
from dbus.gobject_service import ExportedGObject

from jarabe.model import network
