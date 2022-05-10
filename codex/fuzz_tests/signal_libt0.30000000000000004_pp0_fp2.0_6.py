import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from gi.repository import Gtk, Gdk, GObject

from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.activity.widgets import StopButton

from gettext import gettext as _
import os
import logging

from sugargame.canvas import PygameCanvas

import game

class Activity(activity.Activity):
    def __init__(self, handle):
        activity.Activity.__init__(self, handle)

        self.game = game.Game()

        self.max_participants = 1

        # Build the activity toolbar.
        self.build_toolbar()

        # Build the Pygame canvas.
        self._pygamecanvas = PygameCanvas(self)
        self.set_canvas(self._pygamecanvas)
        self._pygamecanvas.grab_focus()
        self._pygamecanvas
