import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from xml.etree import ElementTree
from xml.dom import minidom

from . import resources
from . import __version__
from . import log
logger = log.get_logger(__name__)
from . import utils
from . import settings
from . import template
from . import theme
from . import action
from . import shortcut
from . import syntax
from . import filetype
from . import dock
from . import panels
from . import shell
from . import input_dialog
from . import find_dialog
from . import replace_dialog
from . import text_edit
from . import tab_bar
from . import tab_widget
from . import status_bar
from . import menu_bar
from . import main_window
