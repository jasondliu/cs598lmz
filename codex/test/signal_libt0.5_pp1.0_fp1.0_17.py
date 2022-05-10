import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

#from gi.repository import Gtk, Gdk, GdkPixbuf, GLib
from gi.repository import Gtk, Gdk, GdkPixbuf, GLib
from gi.repository import GObject

from gi.repository import GdkX11
from gi.repository import Gst
Gst.init(None)

from gi.repository import GES
GES.init()

from gi.repository import GstController

from gettext import gettext as _
import os
import sys
import time
import threading
import Queue

from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.activity.widgets import StopButton
from sugar3.activity.widgets import ShareButton
from sugar3.graphics.toolbutton import ToolButton
