import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import re
import subprocess
import time
import threading
import traceback
import Queue
import socket
import struct
import shutil
import tempfile

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from ui_mainwindow import Ui_MainWindow
from ui_about import Ui_AboutDialog
from ui_settings import Ui_SettingsDialog
from ui_new import Ui_NewDialog
from ui_project import Ui_ProjectDialog
from ui_edit import Ui_EditDialog
from ui_new_project import Ui_NewProjectDialog
from ui_new_project_wizard import Ui_NewProjectWizard
from ui_new_project_wizard_page1 import Ui_NewProjectWizardPage1
from ui_new_project_wizard_page2 import Ui_NewProjectWizard
