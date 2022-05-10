import lzma
lzma.LZMAFile = lz.LZMAFile
import io
import os
import datetime

import rdflib
from rdflib.namespace import RDFS

# PyGObject
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import GLib, Gtk, Gdk, GObject, Gio

# Check for bundled/installed scheme files
if os.path.exists(os.path.join(sys.path[0], "..", "data", "gdcatalog.schemas")):
    path = os.path.join(sys.path[0], "..", "data", "gdcatalog.schemas")
else:
    path = "/usr/local/share/glade/schemas/gdcatalog.schemas"

# Set up the paths to fetch CSS and icons
if os.path.exists(os.path.join(sys.path[0], "..", "data")):
    gio_path = "resource:///org/gnome/
