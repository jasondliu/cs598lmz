import _struct
import sys
import time
import traceback

import xbox_read

from ant.base import Node, Message, Event
from ant.base import USB2Driver, USB1Driver

from ant.fs.manager import System, Network
from ant.fs.device import FS310

from collections import deque

from . import util

from .driver import Driver
from .driver import PowerMeterSensors
from .driver import CadenceSensors
from .driver import SpeedSensors
from .driver import PowerMeterSensor
from .driver import CadenceSensor
from .driver import SpeedSensor

from .control import SystemControl
from .control import ProgramControl
from .control import ConsoleControl

from . import sysinfo

# ------------------------------
# --- Driver Constants
# ------------------------------


# ------------------------------
# --- Driver
# ------------------------------

class Driver(Driver):

    # ----- Constructor -----
    def __init__(self):

        super(Driver, self).__init__()

        # --- Pause/Resume ---
        self.paused = False
        self.pause_time
