import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QPixmap, QColor, QImage, QPainter, QRegion, QBrush, QPen, QSpacerItem, QSizePolicy
from PyQt4.QtCore import QObject, pyqtSignal, QSize, QRect, QDir, QPoint, QPointF, QSizeF, QTimer
from PyQt4.QtGui import QFont, QPalette, QWidget, QLabel, QDesktopServices
from PyQt4.QtGui import QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QBoxLayout, QMainWindow
from PyQt4.QtGui import QLineEdit, QMessageBox, QIcon, QFontDatabase, QFontMetrics, QDialog, QApplication
