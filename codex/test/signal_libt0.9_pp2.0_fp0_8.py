import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui

import sys, os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Bror(QtGui.QMainWindow):
    def __init__(self, parent = None):
        super(Bror, self).__init__(parent)

        # Check if good Python version, then launch. Otherwise warn user
