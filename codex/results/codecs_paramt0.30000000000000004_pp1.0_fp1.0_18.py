import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Import the required modules
import sys, os, time, re, subprocess, signal, traceback, string
from optparse import OptionParser

# Import the modules that we need
try:
    import pygtk
    pygtk.require("2.0")
except:
    pass
try:
    import gtk
    import gtk.glade
except:
    sys.exit(1)

# Import the modules that we need
try:
    import pynotify
except:
    pass

# Import the modules that we need
try:
    import gconf
except:
    pass

# Import the modules that we need
try:
    import pyinotify
except:
    pass

# Import the modules that we need
try:
    import glib
except:
    pass

# Import the modules that we need
try:
    import gobject
except:
    pass

# Import the modules that we need
try:
    import pango
except:
    pass

# Import the modules that we
