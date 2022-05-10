import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# QT4 imports
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from PyQt4.QtNetwork import *

from ui.ui_mainwindow import Ui_MainWindow
from ui.ui_logindialog import Ui_LoginDialog
from ui.ui_newuserdialog import Ui_NewUserDialog
from ui.ui_edituserdialog import Ui_EditUserDialog
from ui.ui_settingsdialog import Ui_SettingsDialog
from ui.ui_aboutdialog import Ui_AboutDialog
from ui.ui_editcategorydialog import Ui_EditCategoryDialog
from ui.ui_newcategorydialog import Ui_NewCategoryDialog
from ui.ui_newbookdialog import Ui_NewBookDialog
