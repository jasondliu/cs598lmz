import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QCheckBox, QComboBox, QFileDialog, QTableWidget, QTableWidgetItem, QAction, QVBoxLayout, QHBoxLayout, QGridLayout, QProgressBar, QSizePolicy
from PyQt5.QtGui import QIcon, QPixmap, QFont, QImage, QPainter, QColor, QBrush, QPen, QPainterPath, QTransform
from PyQt5.QtCore import Qt, QThread, QTimer, QSize, QPoint, QPointF, QRect, QRectF, QPropertyAnimation, pyqtProperty
