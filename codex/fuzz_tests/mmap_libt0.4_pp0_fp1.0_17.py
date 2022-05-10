import mmap
import os
import re
import sys
import time
import tty
import termios
import threading
import logging
import argparse
import subprocess
import ConfigParser

from collections import deque

from pymavlink import mavutil
from pymavlink.dialects.v10 import ardupilotmega as mavlink1
from pymavlink.dialects.v20 import ardupilotmega as mavlink2

from MAVProxy.modules.lib import mp_module
from MAVProxy.modules.lib import mp_util
from MAVProxy.modules.lib import mp_settings

if mp_util.has_wxpython:
    from MAVProxy.modules.lib.mp_menu import *

class APMKeyboard(mp_module.MPModule):
    def __init__(self, mpstate):
        super(APMKeyboard, self).__init__(mpstate, "keyboard", "keyboard control module")
        self.add_command('keyboard', self.cmd_keyboard, "keyboard control",
                         ["<status|
