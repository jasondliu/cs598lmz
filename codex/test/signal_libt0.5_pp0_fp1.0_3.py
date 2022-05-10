import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys

from PyQt5.QtCore import pyqtSlot, QObject, QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtQuick import QQuickView
from PyQt5.QtQuickWidgets import QQuickWidget

from PyQt5.QtCore import QSettings, QStandardPaths
from PyQt5.QtCore import QEvent, QTimer
from PyQt5.QtGui import QIcon, QPixmap, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMenu, QAction, QActionGroup, QFileDialog, QMessageBox, QSystemTrayIcon
from PyQt5.QtQml import QQmlApplicationEngine, QQmlComponent, QQmlContext, QQmlEngine
