import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import math
import re

from datetime import datetime
from datetime import timedelta

from PyQt5.QtCore import QObject, QUrl, QTimer, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMessageBox, QSystemTrayIcon, QMenu, QStyle, QStyleOptionToolButton, QStylePainter, QStyleOptionButton
from PyQt5.QtGui import QColor, QIcon, QFont
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtQuick import QQuickView
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtWebKitWidgets import QWebView, QWebPage
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtWebEngine
