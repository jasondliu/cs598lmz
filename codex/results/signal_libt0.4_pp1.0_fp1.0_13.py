import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

from . import model
from . import view
from . import controller
from . import config

def get_config_file():
    """Get the config file to use.  If the file is not found,
    create a default one.
    """
    config_file = os.path.expanduser("~/.config/pyside-example.conf")
    if not os.path.exists(config_file):
        config_file = os.path.expanduser("~/.pyside-example.conf")
        if not os.path.exists(config_file):
            config_file = os.path.join(os.path.dirname(__file__),
                                       "pyside-example.conf")
            if not os.path.exists(config_file):
                config_file = None
