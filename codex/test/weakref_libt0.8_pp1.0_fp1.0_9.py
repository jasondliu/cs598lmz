import weakref
from Qt import QtCore, QtGui, QtWidgets, _loadUi

from avalon import api, maya, io
from avalon.maya.lib import colorfunctions
from avalon.tools import lib as toolsLib
from avalon.vendor import qtawesome


# module level
dialog = None
actions = []
seen_assets = list()
dialog_instance = None

# Fonts
FONT_BOLD = QtGui.QFont()
FONT_BOLD.setBold(True)

