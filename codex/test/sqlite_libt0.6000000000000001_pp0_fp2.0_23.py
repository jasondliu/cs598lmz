import ctypes
import ctypes.util
import threading
import sqlite3
import os
import os.path
import sys
import time
import re
import subprocess
import shutil
import tempfile

from gi.repository import GLib
from gi.repository import Gio
from gi.repository import GObject
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GtkSource
from gi.repository import Gedit
from gi.repository import Pango
from gi.repository import PeasGtk

from gettext import gettext as _

try:
    import cPickle as pickle
except ImportError:
    import pickle

#
# To generate the gtk-doc documentation for this plugin, run:
# gtkdoc-scan --module=gmate --source-dir=gmate --rebuild-sections --rebuild-types -o gmate-docs.xml
# gtkdoc-mkdb --module=gmate --source-dir=gmate --output-format=xml --output-dir=docs --name
