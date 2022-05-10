import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic, QtCore, QtGui

from PyQt5.QtCore import QObject, pyqtSignal

#import MaxiNet
from MaxiNet.Frontend.Gui.GuiServer import GuiServer

#import MaxiNet.Frontend.Gui.gui_main
#import MaxiNet.Frontend.Gui.gui_main_vertical
import MaxiNet.Frontend.Gui.gui_main_dockable
import MaxiNet.Frontend.Gui.gui_main_tab
import MaxiNet.Frontend.Gui.gui_main_tab2
import MaxiNet.Frontend.Gui.gui_main_tab3
import MaxiNet.Frontend.Gui.gui_main_tab
