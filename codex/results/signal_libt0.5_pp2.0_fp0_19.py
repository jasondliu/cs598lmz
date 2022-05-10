import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QPushButton, QCheckBox
from PyQt5.QtWidgets import QMessageBox, QProgressBar
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPainter, QPen, QFont
from PyQt5.QtGui import QBrush, QColor, QPalette
from PyQt5.QtCore import Qt, QPoint, QTimer, QThread, pyqtSignal
from PyQt5.QtCore import QSize
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.Q
