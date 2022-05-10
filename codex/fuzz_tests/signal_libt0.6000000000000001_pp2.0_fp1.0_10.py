import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QProcess, QSettings, QTimer
from PyQt5.QtWidgets import QApplication

import lib.config
from lib.misc import file_type, get_open_files, get_all_open_files
from lib.process import Process
from lib.settings import Settings
from lib.window import Window
from lib.widgets.menu_bar import MenuBar
from lib.widgets.tool_bar import ToolBar
from lib.widgets.status_bar import StatusBar
from lib.widgets.tab_bar import TabBar
from lib.widgets.tab_widget import TabWidget
from lib.widgets.splitter import Splitter
from lib.widgets.editor import Editor
from lib.widgets.file_browser import FileBrowser
from lib.widgets.find_in_files import FindInFiles

class Application(QApplication):
    def __init__(self, args):
        super(Application, self).__init__(args)
       
