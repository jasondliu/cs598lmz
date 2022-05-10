import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import os
import sys
import logging

# fix "cannot import name _psutil_linux"
import subprocess
subprocess.Popen = subprocess.Popen

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore    import QSettings
from PyQt5.QtGui     import QIcon, QFont

# For PyQt new window/popup resize/move actions.
from PyQt5.QtCore    import QSize, Qt, pyqtSlot
from PyQt5.QtGui     import QCursor

from pymol import cmd
from pymol.Qt import QtGui
from pymol.Qt import QtCore
from pymol.Qt import QtWidgets
from pymol.Qt import QtOpenGL

from pymol import __version__ as pymol_version
from pymol import cmd

# local imports
from pymol_launcher
