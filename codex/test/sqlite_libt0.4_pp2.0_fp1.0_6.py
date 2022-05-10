import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os
import time

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui.mainwindow import Ui_MainWindow

from ui.dialogs.about import Ui_AboutDialog
from ui.dialogs.settings import Ui_SettingsDialog
from ui.dialogs.add_new_device import Ui_AddNewDeviceDialog
from ui.dialogs.change_device_name import Ui_ChangeDeviceNameDialog
from ui.dialogs.change_device_address import Ui_ChangeDeviceAddressDialog
from ui.dialogs.change_device_port import Ui_ChangeDevicePortDialog
from ui.dialogs.change_device_password import Ui_ChangeDevicePasswordDialog
from ui.dialogs.change_device_type import Ui_ChangeDeviceTypeDialog
from ui.dialogs.change_device_description import Ui_ChangeDeviceDescriptionDialog
from ui.dialogs.change_device_settings import Ui_ChangeDeviceSettingsDialog

