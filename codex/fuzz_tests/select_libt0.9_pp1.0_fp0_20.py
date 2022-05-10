import select
import tty
import sys
import logging
from pprint import pprint
import csv

from brain.brainState import FSMBrainState
from brain.navigator import Navigator
from brain.rcMgr import RCMgr
from brain.zeroconfListener import ZeroconfListener
from camera.imageProcessor import ImageProcessor
from config.config import config
from vision import visionLink
import util
from util.cruiseControlRunner import CruiseControlRunner
from util.pauseManager import PauseManager
import log
import sensors.encoders
import sensors.sonars

logger = logging.getLogger(__name__)

STATE_DRIVING   = 0
STATE_DONE      = 1

class ManualControl(FSMBrainState):
    def __init__(self, nav):
        super(ManualControl, self).__init__()
        self.nav = nav

    def onActivate(self):
        self.level = 0
        self.nav.setForwardSpeed(-0.2)
        self.nav.step(-90.0)
        sensors.encod
