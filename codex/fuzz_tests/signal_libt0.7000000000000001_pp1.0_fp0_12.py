import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtCore, QtGui
from sas.qtgui.MainWindow.MainWindow import MainWindow

from sas.qtgui.Utilities import IconList
from sas.qtgui.Utilities.GuiUtils import blockSignals

from sas.qtgui.Perspectives.Fitting import Fitting
from sas.qtgui.Perspectives.Calculator import Calculator
from sas.qtgui.Perspectives.Data import Data
from sas.qtgui.Perspectives.Invariant import Invariant
from sas.qtgui.Perspectives.PrCalculator import PrCalculator

from sas.qtgui.Perspectives.DataFitting import DataFitting
from sas.qtgui.Perspectives.DataExplorer import DataExplorer
from sas.qtgui.Perspectives.Batch import Batch
from sas.qtgui.Perspectives.Explore2D import Explore2D
from sas.qtgui.
