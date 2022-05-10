import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys

# -- Locales ----------------------------------------------------

import locale
locale.setlocale(locale.LC_ALL, "")

# -- Configure Qt4 for the desired languages -------------------

import gettext
translator = gettext.translation('gui-task-viewer', './client/share/locale', fallback=True)
translator.install(True)

# -- Import modules ---------------------------------------------

import os, thread
import gobject, gtk
import qt

# -- QT and GTK Dependency --------------------------------------

qt.QTimer.singleShot = gobject.timeout_add #FIXME

# -- Global Variable -------------------------------------------

gui = gtk.Builder()
gui.add_from_file("gui-task-viewer.glade")
main_window = gui.get_object("main_window")
main_window.show_all()

# -- Dialogs -----------------------------------------------------

import gui_error_dlg

# -- MainWindow --------------------------------------------------


