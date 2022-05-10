import ctypes
import ctypes.util
import threading
import sqlite3
import subprocess
import os
import time
import re
import signal

from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from PyQt5.Qt import QApplication
from PyQt5.QtWidgets import QMessageBox

from . import dbus_interface
from . import db
from . import password_dialog
from . import qt_utils
from . import rpc
from . import settings
from . import sync
from . import utils
from .models import core_models
from .models import daemon_models

class Daemon(QObject):
    """
    Class handling the connection to the Bitcoin Core daemon.

    Signals:
    * connected
    * disconnected
    * auth_required
    * auth_rejected
    * auth_accepted
    * auth_invalid
    * auth_registered
    * client_updated
    * new_transaction
        - transaction_id
        - type
        - confirmations
    * new_transactions
    * transactions_changed
    * transactions_updated
    *
