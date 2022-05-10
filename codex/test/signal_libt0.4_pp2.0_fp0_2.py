import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import subprocess
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_main import Ui_MainWindow
from ui_about import Ui_About
from ui_add_package import Ui_AddPackage
from ui_add_repo import Ui_AddRepo
from ui_add_server import Ui_AddServer
from ui_add_server_from_file import Ui_AddServerFromFile
from ui_add_server_from_url import Ui_AddServerFromUrl
from ui_add_server_from_url_dialog import Ui_AddServerFromUrlDialog
from ui_add_server_from_url_dialog_2 import Ui_AddServerFromUrlDialog2
from ui_add_server_from_url_dialog_3 import Ui_AddServerFromUrlDialog3
