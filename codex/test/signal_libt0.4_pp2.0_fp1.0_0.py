import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# PyQt5 modules
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView

# Python modules
import os
import sys
import json
import time
import subprocess
import platform

# This module
import wb_tray
import wb_utils
import wb_config
import wb_dialog_about
import wb_dialog_settings
import wb_dialog_accounts
import wb_dialog_account_edit
import wb_dialog_account_add
import wb_dialog_account_delete
import wb_dialog_account_import
import wb_dialog_account_export
import wb_dialog_account_password
import wb_dialog_account_remove
