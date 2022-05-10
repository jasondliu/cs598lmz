import signal
signal.signal(signal.SIGINT, signal.SIG_DFL) 

#QtCore.QObject.connect(qApp, QtCore.SIGNAL('lastWindowClosed()'), qApp, QtCore.SLOT('quit()'))
#QtCore.QObject.connect(qApp, QtCore.SIGNAL('aboutToQuit()'), qApp, QtCore.SLOT('quit()'))

import matplotlib
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
matplotlib.rcParams['font.size'] = 8

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtGui import QTextCursor

from matplotlib.backends.backend_qt4agg import NavigationTool
