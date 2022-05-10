import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys
import time

from PyQt4 import QtGui, QtCore

import slicer

from slicer.ScriptedLoadableModule import *

#
# SampleData
#

class SampleData(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "Sample Data"
    self.parent.categories = ["Informatics"]
    self.parent.dependencies = []
    self.parent.contributors = ["Jean-Christophe Fillion-Robin (Kitware)"]
    self.parent.helpText = """
    This is an example of scripted loadable module bundled in an extension.
    It performs a
