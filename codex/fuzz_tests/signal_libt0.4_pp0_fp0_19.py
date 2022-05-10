import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# TODO: remove this when the bug is fixed in matplotlib
# see https://github.com/matplotlib/matplotlib/issues/5442
import matplotlib.pyplot as plt
plt.ioff()

import numpy as np
import os
import sys
import time
import traceback

from PyQt5 import QtCore, QtGui, QtWidgets

from . import config
from . import core
from . import gui
from . import utils
from . import workers
from . import widgets

# TODO: refactor this module to remove the "main" function

def main():
    """
    Main function for the GUI.
    """

    # start the Qt application
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('PyMca')
    app.setOrganizationName('PyMca')
    app.setOrganizationDomain('pymca.org')
    app.setApplicationVersion(config
