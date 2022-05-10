import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os

from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GObject
from gi.repository import GdkPixbuf

from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.activity.widgets import StopButton
from sugar3.graphics.toolbutton import ToolButton
from sugar3.graphics.alert import Alert
from sugar3.graphics.icon import Icon

from gettext import gettext as _

from sugargame import canvas

from game import Game

class Activity(activity.Activity):
    def __init__(self, handle):
        activity.Activity.__init__(self, handle)

        self.game = Game()
        self.build_toolbar()

        self.game.canvas.grab_focus()
        self.set_can
