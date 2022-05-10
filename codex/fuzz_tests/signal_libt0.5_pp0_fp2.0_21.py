import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QMessageBox, QInputDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets

from lxml import etree

import sys, os, webbrowser, time, datetime, platform, subprocess, shutil, json
import numpy as np

#import pyqtgraph as pg

#from pyqtgraph.Qt import QtCore, QtGui
#import pyqtgraph.opengl as gl
#from pyqtgraph.dockarea import *

#from pyqtgraph.parametertree import Parameter, ParameterTree, ParameterItem, registerParameterType
#from pyqtgraph.parametertree import types as pTypes

from PyQt5.QtWidgets import *
from PyQt
