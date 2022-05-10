import weakref

from . import _backend
from .. import _core
from .._internals import _get_ref


class _Backend(_backend.Backend):
    """
    Backend implementation for PySide2.

    This backend is currently experimental.
    """

    def __init__(self):
        super().__init__()
        self._main_window = None
        self._main_window_ref = None
        self._main_window_closed = False
        self._main_window_closed_ref = None
        self._main_window_closed_event = None
        self._main_window_closed_event_ref = None

    def _create_window(self, title, x, y, width, height, **kwargs):
        from PySide2.QtWidgets import QApplication, QMainWindow

        app = QApplication.instance()
        if app is None:
            app = QApplication(sys.argv)
        window = QMainWindow()
        window.setWindowTitle(title)
        window.resize(width, height)
        window.
