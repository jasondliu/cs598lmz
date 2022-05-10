import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebKitWidgets import QWebView

from PyQt5.QtGui import QIcon

from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PyQt5.QtNetwork import QNetworkReply

from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtWebKit import QWebPage
from PyQt5.QtWebKit import QWebHistory

from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtPrintSupport import QPrintDialog
from PyQt5.QtPrintSupport import QPrintPreviewDialog

import PyQt5.QtCore

from PyQt5.QtCore import QPoint
from PyQt5.QtCore import QSize
