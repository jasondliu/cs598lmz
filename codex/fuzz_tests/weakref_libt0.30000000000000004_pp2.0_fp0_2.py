import weakref
import time
import sys
import os
import re
import logging
import threading
import traceback
import subprocess

from pymavlink import mavutil
from pymavlink.mavextra import *
from pymavlink.rotmat import Vector3, Matrix3
from pymavlink.quaternion import Quaternion

from MAVProxy.modules.lib import mp_module
from MAVProxy.modules.lib import mp_settings
from MAVProxy.modules.lib import mp_util
from MAVProxy.modules.lib import mp_settings

from MAVProxy.modules.lib.mp_menu import *

class APModule(mp_module.MPModule):
    def __init__(self, mpstate):
        super(APModule, self).__init__(mpstate, "ap", "autopilot control")
        self.add_command('ap', self.cmd_ap, "autopilot control",
                         ["<status|arm|disarm|takeoff|land|rtl|mode>",
                          "<mode>"])
        self.
