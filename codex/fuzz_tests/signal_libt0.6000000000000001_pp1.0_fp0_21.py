import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import gtk
import gobject
import os

#from pyfiledialogs import SaveFileDialog
from pyfiledialogs import SaveFileDialog
from pyfiledialogs import FileDialog
from pyfiledialogs import DirectoryDialog

from datetime import datetime

from data_processor import Data_Processor

from matplotlib.backends.backend_gtkagg import FigureCanvasGTKAgg as FigureCanvas
from matplotlib.figure import Figure

from numpy import arange, pi, sin, cos
from matplotlib.backends.backend_gtkagg import NavigationToolbar2GTKAgg as NavigationToolbar

from pylab import plot, show, savefig, xlim, figure, \
                hold, ylim, legend, boxplot, setp, axes

from matplotlib.widgets import Slider

#from matplotlib.pyplot import subplots, tight_layout

from matplotlib.pyplot import subplots, tight_layout



