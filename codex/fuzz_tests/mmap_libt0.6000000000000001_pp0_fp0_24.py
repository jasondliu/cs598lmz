import mmap
import os
import re

from collections import OrderedDict
from threading import Thread
from time import sleep

from i3pystatus import IntervalModule, formatp
from i3pystatus.core.command import run_through_shell
from i3pystatus.core.util import internet, require

DEFAULT_CRITICAL_LIMIT = 1
DEFAULT_CRITICAL_COMMAND = "systemctl suspend"
DEFAULT_CRITICAL_COMMAND_TIMEOUT = 10
DEFAULT_FORMAT = "{status} {percentage:.0f}%"
DEFAULT_STATUS = {
    "DIS": "↓",
    "CHR": "↑",
    "FULL": "=",
}

POWER_SUPPLY_DIR = "/sys/class/power_supply"

BATTERY_STATUS = {
    "Unknown": "N/A",
    "Charging": "CHR",
    "Discharging": "DIS",
    "Not charging": "DIS",
    "Full": "FULL",
}

BATTER
