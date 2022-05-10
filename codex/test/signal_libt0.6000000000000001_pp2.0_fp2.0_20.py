import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

sys.path.append(os.path.abspath(resource_path('..')))

from GLOBAL_CONSTANTS import *
import GLOBAL_CONSTANTS

from src.Game import *
from gui.MainWindow import *
from gui.WindowManager import *
import gui.WindowManager

from gui.Menu import *
from gui.HelpWindow import *

from src.Main import *

from PyQt5 import QtGui, QtCore, QtWidgets

def main():
    app = QtWidgets.QApplication(sys.argv)

    # We don't use stylesheets.
    app.setStyleSheet("")

    # Set the font.
    fontDB
