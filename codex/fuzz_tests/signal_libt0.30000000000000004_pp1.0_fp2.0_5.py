import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import re
import subprocess
import time
import json

from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, QUrl, QTimer
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QApplication

from . import config
from . import utils
from . import qml_utils
from . import qml_objects
from . import qml_dialogs
from . import qml_settings
from . import qml_downloads
from . import qml_torrents
from . import qml_torrent_details
from . import qml_torrent_peers
from . import qml_torrent_files
from . import qml_torrent_trackers
from . import qml_torrent_webseeds
from . import qml_torrent_options
