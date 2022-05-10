import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import subprocess
import sys

from PyQt5.QtCore import QObject, QUrl, QByteArray, QTimer, QEventLoop
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine

from . import __version__
from . import _qml
from . import _qml_resource
from . import _qml_resource_rc

# This is a hack to make sure the QML engine is correctly initialized.
# In the future, we should probably do this in a more clean way.
_qml.init_qml()

from . import _cached_files
from . import _cached_files_rc
from . import _qml_rc
from . import _qml_rc_rc


class Application(QObject):
    def __init__(self, argv):
        super().__init__()

        self._engine = QQmlApplicationEngine()
        self
