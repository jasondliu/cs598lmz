import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

# PySide2
try:
    from PySide2.QtGui import QGuiApplication
    from PySide2.QtCore import QTimer
except ImportError: # pragma: no cover
    QTimer = None
    QGuiApplication = None

# Create an application instance
if not QCoreApplication.instance() and QGuiApplication is not None:
    app = QGuiApplication([''])
    # Stop the application execution when the event loop is idle
    def exit():
        app.exit(0)
    QTimer.singleShot(0, exit)

import appimagelauncher

from .utils import is_appimage, is_appimage_in_path, get_appimage_exe_path, write_appimage_info, touch, copyfile

from . import logger
from .__version__ import __version__
from .__version__ import __appname__
from .__version__ import __description__
from .__version__ import __url__
from .__version__ import __author__
from .__version__ import __author_email
