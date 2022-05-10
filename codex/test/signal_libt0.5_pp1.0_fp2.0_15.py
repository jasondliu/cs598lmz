import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os, sys

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gdk, GObject, GLib

from . import filer, fileutil, config, util, mount, gio
from .filerwindow import FilerWindow
from .iconview import IconView
from .preferences import Preferences
from .filetype import get_type

from . import sound

# Set up translation support
import gettext
gettext.textdomain('rox-filer')

_ = gettext.gettext

def _(message):
    return gettext.dgettext('rox-filer', message)

# FIXME: Use Gtk.get_default_language()
def _n(single, plural, n):
    return gettext.ngettext('rox-filer', single, plural, n)

