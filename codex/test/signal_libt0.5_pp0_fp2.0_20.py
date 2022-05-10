import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui
from PyQt4.QtCore import QTimer

from lib.config import Config

from lib.gui.main_window import MainWindow
from lib.gui.preferences_dialog import PreferencesDialog

from lib.gui.widgets.status_bar import StatusBar
from lib.gui.widgets.status_bar_item import StatusBarItem

from lib.gui.widgets.tab_widget import TabWidget
from lib.gui.widgets.tab_bar import TabBar

from lib.gui.widgets.tab_icon import TabIcon

from lib.gui.widgets.content_widget import ContentWidget
from lib.gui.widgets.content_tab import ContentTab
from lib.gui.widgets.content_tab_bar import ContentTabBar

from lib.gui.widgets.splitter import Splitter

from lib.gui.widgets.web_view import WebView
from lib.gui.widgets.web_page import WebPage
