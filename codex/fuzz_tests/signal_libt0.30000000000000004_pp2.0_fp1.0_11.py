import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush, QIcon
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal, QObject
from PyQt5 import uic
from PyQt5.Qt import QLabel
from PyQt5.Qt import QPushButton
from PyQt5.Qt import QLineEdit
from PyQt5.Qt import QVBoxLayout
from PyQt5.Qt import QHBoxLayout
from PyQt5.Qt import QSizePolicy
from PyQt5.Qt import QSize
from PyQt5.Qt import QPoint
from PyQt5.Qt import QPainter
from PyQt5.Qt import QPen
from PyQt5.Qt import QColor
