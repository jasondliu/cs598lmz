import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtNetwork import *
import sys
from PyQt5.QtCore import Qt

from file_menu import *
from edit_menu import *
from view_menu import *
from history_menu import *
from tools_menu import *
from help_menu import *
from tb_addressbar import *
from tb_navigation import *
from tb_status import *
from tb_bookmarks import *
from tb_downloads import *
from tb_find import *
from tb_tabs import *
from tb_zoom import *
from tb_developer import *

from window_tabs import *
