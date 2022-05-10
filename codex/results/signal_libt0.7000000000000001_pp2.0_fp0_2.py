import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QUrl
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtWebKitWidgets import QWebView

from PyQt5.QtGui import QGuiApplication, QIcon
from PyQt5.QtWidgets import QApplication, QDesktopWidget

from PyQt5.QtCore import Qt, QTimer, QDateTime, QSize, QPoint, QThread, pyqtSignal
from PyQt5.QtWidgets import QWidget, QListWidget, QVBoxLayout, QListView, QWidgetAction, QToolTip, QMenu, QStyle, QScrollArea, QFileDialog, QDialog, QLabel, QPushButton, QSizePolicy
from PyQt5.QtGui import QFont, QPalette, QColor, QMouseEvent, QContextMenuEvent, QIcon
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
