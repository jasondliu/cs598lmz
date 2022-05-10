import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time
import json
import subprocess
import threading
import traceback

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
gi.require_version('GdkPixbuf', '2.0')
gi.require_version('Pango', '1.0')
gi.require_version('PangoCairo', '1.0')
