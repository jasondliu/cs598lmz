import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
gi.require_version('GtkSource', '3.0')
from gi.repository import Gtk, Gdk, GtkSource, GObject, GLib

from .window import MainWindow

def main():
    GObject.threads_init()
    GLib.set_application_name('Kupfer')
    GLib.set_prgname('kupfer')

    from . import version
    version.check_version(version.VERSION, version.RELEASE)

    MainWindow().show()
    Gtk.main()
