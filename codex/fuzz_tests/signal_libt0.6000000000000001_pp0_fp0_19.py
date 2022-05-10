import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os

import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GObject

from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.activity.widgets import StopButton
from sugar3.graphics.toolbutton import ToolButton
from sugar3.graphics.objectchooser import ObjectChooser

import logging
_logger = logging.getLogger("share-activity")

import gettext
_ = lambda msg: gettext.dgettext("share-activity", msg)

from share_activity import ShareActivity

class ShareActivityInvitation(Gtk.Dialog):

    def __init__(self, activity):
        GObject.GObject.__init__(self)

        self.set_title
