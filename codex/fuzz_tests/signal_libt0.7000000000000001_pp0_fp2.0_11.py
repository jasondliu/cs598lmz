import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os

sys.path.insert(0, os.path.abspath('../'))

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')

from gi.repository import Gtk, Gdk

from yaru_gtk.gtk_css import gtk_css

from yaru_gtk.gtk_settings import gtk_settings

gtk_css()
gtk_settings()

import builder


def main():
    window = builder.MyWindow()

    window.show_all()
    Gtk.main()


if __name__ == '__main__':
    main()
