import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from gi.repository import Gtk, GLib, Gdk
from gi.repository import GObject

import os.path
import sys

from sugar3.activity.activity import Activity
from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.activity.widgets import StopButton
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.graphics.toolbarbox import ToolbarButton

from sugar3.graphics.alert import Alert
from sugar3.graphics.alert import NotifyAlert

from sugar3.graphics.toolbutton import ToolButton
from sugar3.graphics.icon import Icon
from sugar3.graphics import style

from gettext import gettext as _

import logging

log = logging.getLogger('enjoy')

from enjoy import Enjoy as EnjoyWindow
from enjoy import EnjoyApp

class EnjoyActivity(Activity):
    def __init__(self, handle):
        Activity.__init__(self, handle
