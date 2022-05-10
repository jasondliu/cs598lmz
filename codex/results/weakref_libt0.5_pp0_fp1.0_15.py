import weakref

from PySide2.QtCore import QObject, Signal
from PySide2.QtWidgets import QWidget

from . import utils
from .exceptions import NoSuchWidgetError
from .signals import signal_handler
from .testing import wait_signal
from .widgets import Widget


class Application:
    """Helper class to simplify the usage of Qt.

    This class is a wrapper around a QApplication and provides a simple API for
    testing Qt applications.

    The class makes use of the ``QT_AUTO_SCREEN_SCALE_FACTOR`` environment
    variable to enable high DPI support.

    Args:
        widget (QWidget): The widget to test.
    """

    def __init__(self, widget: QWidget):
        self._app = QApplication.instance()
        if self._app is None:
            self._app = QApplication(sys.argv)

        self._widget = widget
        self._widget.show()

        self.wait_for_window_shown()

    def __del__(self):
       
