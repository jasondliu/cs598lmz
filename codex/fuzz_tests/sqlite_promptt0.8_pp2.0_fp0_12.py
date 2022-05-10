import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

# try to import the Glade XML support
try:
    import libglade
except:
    libglade = None

##
# This is a stub module which needs to be replaced with the actual Gtk/Glade/Gnome
# modules.
#

def get_gtk_version():
    "Return the Gtk version as a string"
    if _gtk_version is not None:
        return _gtk_version
    try:
        if _gtk_version is None:
            _import_gtk()
    except Exception:
        pass
    return _gtk_version

def have_pygtk():
    "Return True if pygtk is available"
    if _pygtk_version is not None:
        return True
    try:
        if _pygtk_version is None:
            _import_pygtk()
    except Exception:
        return False
    return True

def have_glade():
    "Return True if Glade support is available"
    if libglade is not None:
