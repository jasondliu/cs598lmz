import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QThread, pyqtSignal, QObject, pyqtSlot

from ui_mainwindow import Ui_MainWindow
from ui_about import Ui_About
from ui_settings import Ui_Settings
from ui_add_server import Ui_AddServer
from ui_edit_server import Ui_EditServer
from ui_add_user import Ui_AddUser
from ui_edit_user import Ui_EditUser
from ui_add_group import Ui_AddGroup
from ui_edit_group import Ui_EditGroup
from ui_add_user_to_group import Ui_AddUserToGroup
from ui_add_server_to_group import Ui_AddServerToGroup
