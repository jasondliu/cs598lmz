import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('amy.PyDictionary')

from PyQt5.QtWidgets import QSystemTrayIcon, QApplication, QMenu, QInputDialog, QLineEdit, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, Qt, QTimer, QPoint, QObject, QEvent, QEventLoop, pyqtSignal, pyqtSlot, QThread
from PyQt5.Qt import QClipboard
from PyQt5 import QtTest
from PyQt5.QtSql import QSqlQueryModel, QSqlRecord, QSqlQuery


from ui.window import Ui_MainWindow
from ui.about import Ui_About
from ui.setting import Ui_Setting
from ui.wordbook import Ui_Wordbook
from ui.addwordbook import Ui_AddWordbook
from ui.update import Ui_Update
from wordbook import Wordbook

from
