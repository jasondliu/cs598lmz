import gc, weakref, sys, webbrowser
from PyQt4 import QtCore, QtGui
import os, traceback
import tempfile

from PyQt4.QtCore import QVariant

from qgis.core import *
from qgis.utils import iface

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class EditDialog(QtGui.QDialog):
    def __init__(self, parent):
        self.parent = parent
        self.plugin = self.parent.plugin
        self.dl
