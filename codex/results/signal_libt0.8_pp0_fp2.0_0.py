import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys
import time
import random
import codecs

# PySide
import PySide
from PySide import QtGui, QtCore

try:
    from PySide.phonon import Phonon
except ImportError:
    try:
        from PyQt4.phonon import Phonon
    except ImportError:
        gettext.install("gmusicbrowser", unicode=1)
        QtGui.QMessageBox.critical(None,_("Error !"),_("you need phonon.\nTry installing python-qt4-phonon or phonon-backend-vlc"))
        sys.exit(1)

def debug(*args):
    print >>sys.stderr, " ".join(map(str, args))

#py2exe needs the following
import py2exe_util

def list2cmdline(list):
    if sys.platform=='win32':
        return subprocess.list2cmdline(list)
   
