import weakref
import logging

from .. import qt_api

from ..utils.logs import logger

if qt_api == 'pyqt':
    from PyQt4.QtCore import QObject, QCoreApplication, QEvent, QTimer
    from PyQt4.QtGui import QApplication
    from PyQt4.QtCore import pyqtSignal as Signal
    from PyQt4.QtCore import pyqtProperty as Property
elif qt_api == 'pyqt5':
    from PyQt5.QtCore import QObject, QCoreApplication, QEvent, QTimer
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtCore import pyqtSignal as Signal
    from PyQt5.QtCore import pyqtProperty as Property
elif qt_api == 'pyside':
    from PySide.QtCore import QObject, QCoreApplication, QEvent, QTimer
    from PySide.QtGui import QApplication
    from PySide.QtCore import Signal
