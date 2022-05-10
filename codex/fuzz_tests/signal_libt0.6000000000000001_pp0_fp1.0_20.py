import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject
from PyQt5.QtCore import QThread
from PyQt5.QtCore import QMutex
from PyQt5.QtCore import QSize
from PyQt5.QtCore import QMutexLocker
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QSizeF
from PyQt5.QtCore import QPointF
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import QDir
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QEvent
from PyQt5.QtCore import QTimer

