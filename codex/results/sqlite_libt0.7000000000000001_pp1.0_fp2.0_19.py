import ctypes
import ctypes.util
import threading
import sqlite3
import os
import shutil
import time

try:
    import queue
except ImportError:
    import Queue as queue

try:
    import libvirt
except ImportError:
    if sys.version_info[0] < 3:
        raise RuntimeError("pygobject >= 3.0.0 is required for python2")
    elif sys.version_info[1] < 6:
        raise RuntimeError("pygobject >= 3.6.0 is required for python3")

try:
    import gi
    gi.require_version("Gtk", "3.0")
    from gi.repository import Gtk, Gdk, GLib, GObject
    from gi.repository.GdkPixbuf import Pixbuf
except ImportError:
    raise RuntimeError("pygobject is required for this application")

try:
    import ifaddr
except ImportError:
    raise RuntimeError("ifaddr is required for this application")

try:
    import netifaces
except ImportError:
    raise RuntimeError("netifaces is required for
