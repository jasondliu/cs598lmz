import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.QtGui import QIcon

from ui_mainwindow import Ui_MainWindow
from ui_about import Ui_AboutDialog
from ui_settings import Ui_SettingsDialog
from ui_add_connection import Ui_AddConnectionDialog

import os
import sys
import subprocess
import configparser
import shutil

import paramiko
import socket

import functools

from pprint import pprint

import logging

import pkg_resources

class SettingsDialog(QDialog):
    def __init__(self):
        super(SettingsDialog, self).__init__()
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self
