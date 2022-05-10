import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebChannel import *

from ui_mainwindow import Ui_MainWindow
from ui_aboutdialog import Ui_AboutDialog
from ui_preferencesdialog import Ui_PreferencesDialog
from ui_bookmarkdialog import Ui_BookmarkDialog
from ui_downloaddialog import Ui_DownloadDialog
from ui_historydialog import Ui_HistoryDialog
from ui_historylistdialog import Ui_HistoryListDialog
from ui_historylistitem import Ui_HistoryListItem
from ui_bookmarklistdialog import Ui_BookmarkListDialog
from ui_bookmarklistitem import Ui_BookmarkListItem
from ui_downloadlistdialog import Ui
