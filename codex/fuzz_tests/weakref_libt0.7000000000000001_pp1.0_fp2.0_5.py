import weakref

from PySide import QtGui as qt

from .. import api
from .. import signals
from .. import utils


class _Controller(object):

    def __init__(self, window, item):
        self._window = weakref.ref(window)
        self._item = weakref.ref(item)

    def _window_deleted(self, widget):
        self._window = None
        self._window_deleted = None

    def _item_deleted(self, item):
        self._item = None
        self._item_deleted = None


class Window(object):

    def __init__(self, item=None, parent=None):
        self._window = qt.QMainWindow()
        self._window.setCentralWidget(qt.QWidget())
        self._window.centralWidget().setLayout(qt._QBoxLayout(2))
        self._window.centralWidget().layout().setContentsMargins(4, 4, 4, 4)
        self._window.centralWidget().layout().setSpacing(6)
        self._window.
