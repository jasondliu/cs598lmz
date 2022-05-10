import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

#
# The following is necessary for running under Python 3.2.3:
#
if sys.version_info >= (3,):
    import imp
    imp.reload(sys)
#
# End of code for Python 3.2.3
#

import os
import traceback
import re
import random
import time
import threading

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit', '3.0')

from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GObject
from gi.repository import WebKit

from gettext import gettext as _

import sugar3.activity.activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.activity.widgets import StopButton
from sugar3.graphics.toolbutton import ToolButton
