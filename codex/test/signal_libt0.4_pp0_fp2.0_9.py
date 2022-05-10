import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebEngineWidgets import QWebEngineSettings

app = QApplication(sys.argv)

web = QWebEngineView()
web.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
web.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
web.settings().setAttribute(QWebEngineSettings.JavascriptCanOpenWindows, True)
web.settings().setAttribute(QWebEngineSettings.JavascriptCanAccessClipboard, True)
web.settings().setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
web.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
web.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)

