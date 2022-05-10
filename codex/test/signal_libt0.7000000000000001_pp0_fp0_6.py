import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
from PySide import QtGui, QtCore
import os
from functools import partial
from collections import OrderedDict
from createNode import *
import maya.cmds as cmds
import maya.mel as mel
from functools import partial
import time
from PySide.QtGui import *
from PySide.QtCore import *
from cStringIO import StringIO
import operator
from PySide import QtUiTools
from PySide.QtGui import QColor, QBrush
import pymel.core as pymel
import maya.mel as mel
import maya.OpenMayaUI as omui
from shiboken import wrapInstance
from pprint import pprint


def getMayaWindow():
    ptr = omui.MQtUtil.mainWindow()
