import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys
import datetime
import time

from PyQt5 import QtCore, QtWidgets
from scribus import *

import about
import export_dialog
import import_dialog
import pdf_dialog
import print_dialog
import preferences
import send_dialog
import tooltip

if haveUI:
    _ = setlanguage()


try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


def log(message):
    now = datetime.datetime.now()
