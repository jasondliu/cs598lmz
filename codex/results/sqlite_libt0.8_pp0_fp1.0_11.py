import ctypes
import ctypes.util
import threading
import sqlite3
import urllib
import re
import sys
import time
import glob
import os
import xml.sax.saxutils
import logging

from gi.repository import GObject
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GdkPixbuf
from gi.repository import Gio
from gi.repository import GtkSource
from gi.repository import Pango
from gi.repository import GtkSpell
from gi.repository import GLib
from gi.repository import Gedit

from gettext import gettext as _

try:
    import psutil
except ImportError:
    psutil = None

import gtkgui_helpers
import gedit_terminal
import gedit_latex
import pluma_prefs
import gtkspellcheck
import prettify
import gedit_parser
import gedit_document

from pluma_prefs import PrefsDialog

#logging.basicConfig(level=
