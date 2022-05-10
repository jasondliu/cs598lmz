import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PySide import QtCore, QtGui

from . import settings
from . import utils


def get_app_icon():
    """
    Returns the app icon.
    """
    return QtGui.QIcon(utils.get_icon_path("icon.png"))


def get_app_icon_pixmap(size=None):
    """
    Returns the app icon as a pixmap.
    """
    return QtGui.QPixmap(utils.get_icon_path("icon.png"), "PNG")


def get_app_icon_pixmap_from_base64(base64_data, size=None):
    """
    Returns the app icon as a pixmap from base64 data.
    """
    data = QtCore.QByteArray.fromBase64(base64_data)
    pixmap = QtGui.QPixmap()
    pixmap.loadFromData(data)
    return pixmap


def
