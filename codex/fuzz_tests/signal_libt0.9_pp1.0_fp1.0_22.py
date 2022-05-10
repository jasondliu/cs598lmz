import signal
signal.signal(signal.SIGINT, signal.SIG_DFL) # enable CTRL-C again

# QT stuff
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtGui import QPalette, QColor, QFont
import pyqtgraph as pg

pg.setConfigOption('background', (20,20,20))
pg.setConfigOption('foreground', (255,255,255))
pg.setConfigOption('antialias', True)

# scipy and friends
import matplotlib as mpl
mpl.use('Qt4Agg')
mpl.rcParams['axes.linewidth'] = 1.2
import matplotlib.pyplot as plt
#import scipy.cluster.hierarchy as sch
import matplotlib.dates as mdates

plt.style.use('ggplot')


#import scipy.signal

# local files

