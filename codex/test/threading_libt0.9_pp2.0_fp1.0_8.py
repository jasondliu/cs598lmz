import threading
threading.currentThread().setName('MainThread')

# qtpy
import qtpy
from qtpy.QtCore import QPoint, Qt
from qtpy.QtGui import (QGuiApplication, QShowEvent, QWindow, QColor,
                        QKeyEvent)
from qtpy.QtWidgets import (QAction, QActionGroup, QShortcut, QMenu,
                        QKeySequence,
                        QStyle, QStyleFactory, QLabel, QGraphicsOpacityEffect,
                        QFrame, QStackedWidget, QPushButton, QHBoxLayout,
                        QVBoxLayout, QWidget, QSizePolicy, QMenuBar,
                        QStyleOption)
if qtpy.PYQT5:
    from qtpy.QtMultimedia import QCamera, QCameraInfo, QCameraViewfinder, QCameraImageCapture


from qtpyvcp.plugins import getPlugin
from qtpyvcp.utilities import logger
