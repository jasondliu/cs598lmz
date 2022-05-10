import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui_main import Ui_MainWindow
from ui_about import Ui_AboutWindow
from ui_settings import Ui_SettingsWindow
from ui_add import Ui_AddWindow
from ui_edit import Ui_EditWindow
from ui_play import Ui_PlayWindow
from ui_help import Ui_HelpWindow
from ui_reset import Ui_ResetWindow
from ui_import import Ui_ImportWindow

import os
import sys
import json
import subprocess
import shutil
import random
import sqlite3

from datetime import datetime
from multiprocessing import Process
from multiprocessing import Queue
from subprocess import Popen, PIPE
from PyQt4.QtGui import
