import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from gi.repository import Gtk, Gdk

from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.activity.widgets import StopButton
from sugar3.activity.widgets import EditToolbar
from sugar3.graphics.toolbutton import ToolButton
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.graphics.toolbarbox import ToolbarButton
from sugar3.activity.widgets import ActivityToolbarMenuButton
from sugar3.activity.widgets import ShareButton
from sugar3.graphics.toolbarbox import ToolbarButton
from sugar3.graphics.radiotoolbutton import RadioToolButton
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityToolbarMenuButton
from sugar3.activity.widgets import ShareButton

from gettext import gettext as _


class Activity(Gtk.Activity):
    def __init__(self, handle):
        Gtk.Activity.
