import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
if 'DISPLAY' not in os.environ:
    import matplotlib
    matplotlib.use('Agg')

from PyQt5 import QtCore, QtWidgets

from orangewidget import gui
from orangewidget.settings import Setting
from oasys.widgets import gui as oasysgui, congruence
from oasys.util.oasys_util import EmittingStream, TTYGrabber, TriggerIn, TriggerOut

from orangecontrib.srw.util.srw_objects import SRWData
from orangecontrib.srw.widgets.gui.ow_srw_input_element import SRWInputElement
from orangecontrib.srw.widgets.gui.ow_srw_optical_element import SRWOpticalElement
from orangecontrib.srw.widgets.gui.ow_srw_source import SRWSource
from orangecontrib.srw.widgets.gui.ow_srw_process import SR
