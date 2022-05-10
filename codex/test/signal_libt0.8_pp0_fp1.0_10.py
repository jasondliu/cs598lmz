import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
gi.require_version('Pango', '1.0')
gi.require_version('PangoCairo', '1.0')
gi.require_version('GdkPixbuf', '2.0')
from gi.repository import Gio, Gtk, Gdk, Pango, PangoCairo, GdkPixbuf

from dbus import SessionBus
from dbus.exceptions import DBusException

from pisak import logging, config, helpers, events, test

LOG = logging.get_logger(__name__)
"""Main application logger"""


class Application(Gtk.Application):
    """
    Pisak application.

    Main application class, from which all other application windows
    are created.
    """

