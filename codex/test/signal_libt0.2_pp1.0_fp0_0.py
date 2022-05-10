import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time
import threading
import traceback
import subprocess

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui.mainwindow import Ui_MainWindow
from ui.about import Ui_About
from ui.preferences import Ui_Preferences

from ui.preferences import Preferences
from ui.about import About
from ui.mainwindow import MainWindow

from ui.widgets.qrcodewidget import QRCodeWidget
from ui.widgets.qrtextedit import QRTextEdit
from ui.widgets.qrlineedit import QRLineEdit

from electrum_gxx.i18n import _
