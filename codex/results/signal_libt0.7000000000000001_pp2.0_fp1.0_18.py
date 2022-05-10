import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from ui_mainwindow import Ui_MainWindow
from ui_add_new_user import Ui_add_new_user_dialog
from ui_edit_user import Ui_edit_user_dialog
from ui_about_dialog import Ui_aboutDialog
from ui_settings_dialog import Ui_settingsDialog
from ui_create_new_db import Ui_create_new_db_Dialog
from ui_login_dialog import Ui_loginDialog

from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime

from settings import *
from db import *

from functools import partial

import sys

class SettingsDialog(QDialog, Ui
