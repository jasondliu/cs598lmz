import signal
signal.signal(signal.SIGINT,signal.SIG_DFL)

from PySide import QtGui, QtCore
from maya import cmds, mel
import maya.OpenMayaUI as omui
from shiboken import wrapInstance
import logging
import panel
from parameters import *


# initialise the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('setup.log')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)


class MyToolBar(QtGui.QWidget):

	def __init__(self, name, icon_path, shortcut, parent=None):
		super(MyToolBar, self).__init
