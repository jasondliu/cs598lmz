import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QFileDialog, QInputDialog, QLineEdit, QDialog
from PyQt5.QtCore import QThread, pyqtSignal, QObject, pyqtSlot, QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QSize
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import QPointF
from PyQt5.QtCore import QEvent
from PyQt5.QtCore import QMargins
from PyQt5.QtCore import QSettings
from PyQt5.QtCore import QSizeF
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QUrl
