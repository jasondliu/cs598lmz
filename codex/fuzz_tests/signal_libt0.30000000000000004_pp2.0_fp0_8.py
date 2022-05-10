import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit, QMessageBox, QFileDialog, QTableWidget, QTableWidgetItem, QAbstractItemView, QHeaderView, QToolTip, QMenu, QAction, QMenuBar, QStatusBar, QComboBox, QCheckBox, QListWidget, QListWidgetItem, QListView, QSizePolicy, QSlider, QSpinBox, QStyleFactory, QProgressDialog, QDialog, QGridLayout, QGroupBox, QRadioButton, QButtonGroup, QTabWidget, QFrame, QTreeWidget, QTreeWidgetItem, QTreeView
from PyQt5.QtGui import QIcon, QFont, QPixmap, QImage, QColor, QPalette, QBrush
