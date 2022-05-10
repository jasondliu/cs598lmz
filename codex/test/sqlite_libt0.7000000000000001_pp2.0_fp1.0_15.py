import ctypes
import ctypes.util
import threading
import sqlite3
import datetime
import math

import PyQt4.QtCore
import PyQt4.QtGui
import PyQt4.QtSql
import PyQt4.uic
import rtmidi_python as rtmidi
import numpy

from . import midi
from . import db
from . import dsp
from . import const
from . import util
from . import audio
from . import gui
from . import events
from . import synth
from . import effects

from .config import config
from . import config

from . import version

import logging
log = logging.getLogger(__name__)

class Main(QtGui.QMainWindow):

  def __init__(self):
    super(Main, self).__init__()

    # load UI
    self.ui = PyQt4.uic.loadUi("frontend.ui", self)

    # setup audio
    self.audio = audio.Audio()

    # setup GUI
    self.ui.setup(self)

    # setup synth

