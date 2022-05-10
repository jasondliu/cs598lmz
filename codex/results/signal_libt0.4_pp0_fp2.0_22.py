import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication

import sys
import os

from PyQt5.QtCore import Qt
from PyQt5.QtCore import QSize
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QEvent
from PyQt5.QtCore import QObject
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QSettings
from PyQt5.QtCore import QByteArray
from PyQt5.QtCore import QDir
from PyQt5.QtCore import QStandardPaths
from PyQt5.QtCore import QFileInfo
from PyQt5.QtCore import QDirIterator
from PyQt5.QtCore import QFile
from PyQt5.QtCore import Q
