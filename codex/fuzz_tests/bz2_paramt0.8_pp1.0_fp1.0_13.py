from bz2 import BZ2Decompressor
BZ2Decompressor.decompress

import sys
import re
import urllib2
import os
import time
import shutil
from stat import *

from utils import *

# FreeCAD
import FreeCAD, FreeCADGui, Part
import DraftGeomUtils, Mesh
from FreeCAD import Base
from FreeCAD import Vector

import Mesh

# Qt library
from PyQt4 import QtCore, QtGui

from DraftTools import translate

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig
