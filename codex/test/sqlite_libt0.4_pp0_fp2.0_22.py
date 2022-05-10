import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
import os
import re
import codecs
import copy
import logging

# import the Qt libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import uic

# import the GUI files
from gui.ui_mainwindow import Ui_MainWindow
from gui.ui_add_account_dialog import Ui_AddAccountDialog
from gui.ui_add_contact_dialog import Ui_AddContactDialog
from gui.ui_add_group_dialog import Ui_AddGroupDialog
from gui.ui_add_server_dialog import Ui_AddServerDialog
from gui.ui_change_password_dialog import Ui_ChangePasswordDialog
from gui.ui_chat_dialog import Ui_ChatDialog
from gui.ui_contact_info_dialog import Ui_ContactInfoDialog
from gui.ui_edit_account_dialog import Ui_EditAccountDialog
from gui.ui_edit_contact_dialog import Ui_EditContactDialog
