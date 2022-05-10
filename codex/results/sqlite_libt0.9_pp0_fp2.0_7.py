import ctypes
import ctypes.util
import threading
import sqlite3
import codecs
# from . import core as core
# from .util import log
# from . import glv as globalvars


def get_icon_by_id(icon_id):
    """Get a custom icon (from theme or index) and return a QIcon(QPixmap)
    and it's size.
    """
    icon_size = None
    icon = None

    icon_path = ThemeLoader.load_theme('icons/' + icon_id)
    if icon_path is not None:
        # qimg = QImage(str(icon_path))
        # if not qimg.isNull():
        #     icon_size = qimg.size()
        #     icon = QIcon(QPixmap.fromImage(qimg))
        # else:
        #     log.error('Icon not valid:', icon_path)
        icon_size = tuple(64, 64)
        icon = QIcon(str(icon_path))
    else:
        # Icon names should be numbers, raise warning if not,
        # because this may be quite confusing
