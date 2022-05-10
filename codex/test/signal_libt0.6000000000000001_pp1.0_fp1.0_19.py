import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import sys
import os
import gtk
import gobject
import pango
import time

try:
    import glib
except:
    import gobject as glib

import pynotify
if not pynotify.init('Notification'):
    sys.exit(1)

