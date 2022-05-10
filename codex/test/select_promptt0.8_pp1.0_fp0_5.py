import select
# Test select.select() call and poll() in the glib event loop.
# For the test we have three read pipes and one write pipe.
# The first read pipe is writing 100 bytes of data at a time.
# The second read pipe is writing 500 bytes of data at a time.
# The third read pipe is writing 1000 bytes of data at a time.

import signal
import time

import gi

from gi.repository import GLib, GObject

