import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from PyQt4.QtNetwork import *

from ui_mainwindow import Ui_MainWindow
from ui_about import Ui_About

from settings import Settings
from login import LoginDialog
from utils import get_path, get_icon, get_resource, get_cache_file, get_cookie_file, get_data_file, get_data_path
from utils import open_file, open_url, get_url_info, get_url_data
from utils import get_local_ip, get_local_mac, get_local_name, get_local_hostname
from utils import get_local_os, get_local_cpu, get_local_mem, get_local_disk
from utils import get_local_time, get_local
