import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4.QtCore import (Qt, QTranslator, QTimer, SIGNAL, QFile,
        QTextStream, QStringList, QFileInfo, QProcess)
from PyQt4.QtGui import (QApplication, QSystemTrayIcon, QMenu,
        QAction, QDesktopServices, QIcon, QMessageBox, QFileDialog)
from option_dialog import OptionDialog
from hicolor_icon import set_high_dpi_aware
from daemonize import daemonize
from twisted.internet import reactor
from schemas import *

from gnotifier_rc import *
from gnotifier_tr import *


def qTranslate(app, text, comment=None):
    return QApplication.translate(app, text, comment, QApplication.UnicodeUTF8)


class GnotifierTrayIcon(QSystemTrayIcon):

    def __init__(self, app):
        set_high_dpi_aware()
        QSystem
