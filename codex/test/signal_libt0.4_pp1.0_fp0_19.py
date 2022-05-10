import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import os.path
import subprocess
import time

from gi.repository import Gtk
from gi.repository import GObject

from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.activity.widgets import StopButton
from sugar3.graphics.toolbarbox import ToolbarButton
from sugar3.activity.widgets import ShareButton

from gettext import gettext as _

import logging
_logger = logging.getLogger('memorizar-activity')

class MemorizarActivity(activity.Activity):
    def __init__(self, handle):
        activity.Activity.__init__(self, handle)

        self.set_title(_('Memorizar'))
        self.max_participants = 1

        toolbar_box = ToolbarBox()

        activity_button = ActivityToolbarButton(self)
