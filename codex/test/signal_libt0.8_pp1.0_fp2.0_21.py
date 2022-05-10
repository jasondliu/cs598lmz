import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import (pyqtSignal, QByteArray, QDataStream, QIODevice,
        QObject, QSize, Qt, QPoint, QTimer, QVariant)
from PyQt5.QtGui import (QColor, QDrag, QIcon, QPixmap)
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
        QDialogButtonBox, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QListWidget, QMenu, QMessageBox, QPushButton, QSpinBox, QStyle, QSystemTrayIcon,
        QTextEdit, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QToolTip, QTextBrowser, QTableView,
        QAbstractItemView, QHeaderView)
from PyQt5 import QtWidgets, QtCore, QtGui
