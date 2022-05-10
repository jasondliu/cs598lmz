import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import pickle

from PyQt5.QtCore import Qt, QTimer, QThread, QObject, pyqtSignal
