import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import os.path
import time
import threading
import subprocess
import traceback

from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GObject
from gi.repository import GdkPixbuf
from gi.repository import GLib

from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.activity.widgets import StopButton
from sugar3.graphics.toolbutton import ToolButton
from sugar3.graphics.alert import Alert
from sugar3.graphics.objectchooser import ObjectChooser
from sugar3.graphics.alert import NotifyAlert
from sugar3.graphics.alert import ConfirmationAlert
from sugar3.graphics.toggletoolbutton import ToggleToolButton
from sugar3.graphics.toolbarbox import ToolbarButton
from sugar
