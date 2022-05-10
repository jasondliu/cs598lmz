import gc, weakref
import logging
import pytest

from pytestqt.qt_compat import qt_api
from pytestqt.qt_compat import qt_api_version
from pytestqt.qt_compat import qt_version_info

from pytestqt.logging import _LoggingHandler, _LoggingFormatter

from pytestqt.qt_compat import qt_api
from pytestqt.qt_compat import qt_api_version
from pytestqt.qt_compat import qt_version_info

if qt_api == 'pyside':
    from PySide.QtCore import QObject
    from PySide.QtGui import QApplication
    from PySide.QtSvg import QSvgWidget
    from PySide.QtWebKit import QWebPage
    from PySide.QtWebKit import QWebView
    from PySide.QtNetwork import QNetworkAccessManager
    from PySide.QtNetwork import QNetworkRequest
elif qt_api == 'pyqt5':
    from PyQt5
