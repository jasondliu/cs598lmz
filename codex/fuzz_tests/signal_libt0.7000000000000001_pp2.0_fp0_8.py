import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import json
import os
import sys
import time

from PyQt5.QtCore import QPoint, QSize, Qt, QUrl
from PyQt5.QtGui import QClipboard, QPalette, QPixmap
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QMediaPlaylist
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkProxy, QNetworkProxyFactory, QNetworkReply
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtWebKitWidgets import QWebPage
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog,
        QGridLayout, QInputDialog, QLineEdit, QMenu, QMessageBox,
        QPushButton, QSizePolicy, QToolBar, QVBoxLayout, QWidget)

from qt
