import weakref

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import pyqtgraph as pg

from . import Experiment
from . import dataTypes
from .. import global_vars as g
from .. import QtGui
from .. import QtWidgets
from .. import utils
from .. import config
from .. import resources

class Task(object):
    """
    Base class for defining tasks. Each task must define the following:
    
    __init__
    start
    stop
    save
    load
    close
    event
    paint
    """
    def __init__(self, name):
        self.name = name
        self.experiment = None
    def start(self):
        """Set up everything needed to start this task."""
        pass
    def stop(self):
        """Stop the task and clean up."""
        pass
    def save(self):
        """Save the state of this task."""
        return {}
    def load(
