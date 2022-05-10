import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui_mainwindow import Ui_MainWindow
from ui_about import Ui_About
from ui_preferences import Ui_Preferences
from ui_new import Ui_New

from ui_new_project import Ui_NewProject
from ui_new_file import Ui_NewFile
from ui_new_folder import Ui_NewFolder

from ui_new_cpp import Ui_NewCpp
from ui_new_c import Ui_NewC
from ui_new_java import Ui_NewJava
from ui_new_python import Ui_NewPython
from ui_new_ruby import Ui_NewRuby
from ui_new_html import Ui_NewHtml
from ui_new_css import Ui_NewCss
from
