import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

try:
    from PyQt5.QtWebKit import QWebSettings
    QWebSettings.globalSettings().setAttribute(QWebSettings.PluginsEnabled, True)
except:
    pass


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt, QUrl, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMenu, QAction, QVBoxLayout, QSizePolicy, QMessageBox, QWidget
from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtNetwork import QNetworkProxyFactory, QNetworkProxy

from core.config import config
from core.utils import log
from core.browser import BrowserView
from core.tabs import Tabs
