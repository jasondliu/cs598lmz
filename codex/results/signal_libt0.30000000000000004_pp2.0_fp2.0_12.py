import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QGridLayout, QLabel, QLineEdit, QMessageBox, QFileDialog, QTableWidget, QTableWidgetItem, QComboBox, QDialog, QDialogButtonBox, QFormLayout, QProgressBar, QSizePolicy
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QComboBox, QDialog, QDialogButtonBox, QFormLayout, QProgressBar, QSizePolicy
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QThread
