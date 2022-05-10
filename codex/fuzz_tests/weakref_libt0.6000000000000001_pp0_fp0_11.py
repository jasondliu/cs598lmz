import weakref

from fsui.qt import QApplication, QDesktopWidget, QImage, QLabel, \
    QPixmap, Qt, QWidget, Signal
from fsui.qt.helper import get_icon
from fsui.qt.widget import Widget
from fsui.qt.window import Window
from fsui.qt.window_backend import WindowBackend
from fsui.qt.window_backend_manager import WindowBackendManager
from fsui.qt.window_icon import WindowIcon
from .application_backend import ApplicationBackend
from .dialog_backend import DialogBackend
from .resize_event import ResizeEvent
from .window_flags import WindowFlags
from ..i18n import gettext
from ..signal import Signal
from .window_backend import WindowBackend


class QWindow(WindowBackend, QWidget):

    resized = Signal()
    closing = Signal()

    # noinspection PyArgumentList
    def __init__(self, parent, title, flags=WindowFlags.WINDOW):
        QWidget.
