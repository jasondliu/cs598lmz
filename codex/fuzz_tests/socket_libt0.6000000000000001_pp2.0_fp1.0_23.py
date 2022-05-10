import socket
import sys
import threading
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Ui_login import Ui_Login_Dialog
from Ui_register import Ui_Register_Dialog
from Ui_main_window import Ui_Main_Window


class Login(QDialog, Ui_Login_Dialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("登录")
        self.pushButton.clicked.connect(self.loginButtonClicked)
        self.pushButton_2.clicked.connect(self.regisButtonClicked)
        self.username.returnPressed.connect(self.loginButtonClicked)
        self.password.returnPressed.connect(self.loginButtonClicked)
