import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebEngineWidgets import QWebEngineSettings
from PyQt5.QtWebEngineWidgets import QWebEngineProfile
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon

from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File
from twisted.python import log
from twisted.logger import Logger, LogLevelFilterPredicate, FilteringLogObserver, textFileLogObserver
from twisted.logger import globalLogPublisher, LogLevel, LogLevelFilterPredicate, LogPublisher, textFileLogObserver
