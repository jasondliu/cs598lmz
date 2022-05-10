import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GObject
from gi.repository import GdkPixbuf
from gi.repository import GLib
from gi.repository import Gio

from sugar3.activity.widgets import ActivityButton
from sugar3.activity.widgets import StopButton
from sugar3.activity.widgets import ShareButton
from sugar3.activity import activity
from sugar3 import mime
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.graphics.toolbarbox import ToolbarButton
from sugar3.graphics.toolbutton import ToolButton
from sugar3.graphics.alert import ErrorAlert
from sugar3.graphics.alert import NotifyAlert
from sugar3.graphics.alert import ConfirmationAlert
from sugar3.graphics import style
from sugar3.graphics.icon import Icon
from sugar3.graphics.xocolor import X
