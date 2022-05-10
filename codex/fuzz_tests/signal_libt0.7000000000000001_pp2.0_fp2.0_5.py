import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import pyqtSlot, QTimer, QObject, QPoint
from PyQt5.QtCore import QUrl, Qt, QEventLoop
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtGui import QMouseEvent

from . import _pywebview
from .js import JSObject, wrap_js_class, js_callback
from .js import PyObject, wrap_py_objects, expose_api
from . import local_http_server
from .local_http_server import LocalServer


class BrowserView(QWebEngineView):
    def __init__(self, window, parent=None, enable_inspector=False, user_agent=None, suppress_message_box=False,
                 enable_webgl=False):
        super(Browser
