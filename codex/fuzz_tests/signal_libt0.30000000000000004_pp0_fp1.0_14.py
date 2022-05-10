import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# import the Qt4Agg FigureCanvas object, that binds Figure to
# Qt4Agg backend. It also inherits from QWidget
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# import the NavigationToolbar Qt4Agg widget
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar

# Matplotlib Figure object
from matplotlib.figure import Figure

# Dialog box for file selection
from PyQt4.QtGui import QFileDialog

# Import the PyQt4 module we'll need
from PyQt4.QtCore import QTimer
from PyQt4.QtGui import QApplication

# Import the PyQt4 module we'll need
from PyQt4.QtCore import QSize, Qt
from PyQt4.QtGui import QApplication, QMainWindow, QWidget,
