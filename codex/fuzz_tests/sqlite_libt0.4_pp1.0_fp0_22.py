import ctypes
import ctypes.util
import threading
import sqlite3
import os

from PyQt5.QtCore import (QObject, QThread, QTimer, QCoreApplication,
                          QMutex, pyqtSignal, pyqtSlot)

from PyQt5.QtDBus import QDBusConnection, QDBusInterface, QDBusReply

from . import utils

class DBusServer(QObject):
    def __init__(self, parent, app_id, app_name, app_version,
                 app_description, app_license, app_website,
                 app_logo, app_icon, app_exec, app_path,
                 app_categories):
        super(DBusServer, self).__init__(parent)

        self.app_id = app_id
        self.app_name = app_name
        self.app_version = app_version
        self.app_description = app_description
        self.app_license = app_license
        self.app_website = app_website
        self.app_logo = app_logo
        self.app
