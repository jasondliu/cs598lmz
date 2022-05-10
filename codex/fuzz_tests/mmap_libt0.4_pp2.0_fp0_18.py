import mmap
import os
import struct
import sys
import time

from . import _ioctl
from . import _libc
from . import _util

# ------------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------------

# A set of constants that can be used to determine the type of a device.
#
# NOTE: The values are taken from the Linux kernel header file
#       include/uapi/linux/input.h.
#
# NOTE: The values are not guaranteed to be the same on all platforms.
#       However, they are the same on Linux and OS X.
EV_SYN = 0x00
EV_KEY = 0x01
EV_REL = 0x02
EV_ABS = 0x03
EV_MSC = 0x04
EV_SW = 0x05
EV_LED = 0x11
EV_SND = 0x12
EV_REP = 0x14
EV_FF = 0x15
EV_PWR = 0x16
EV_FF_STATUS = 0x17
EV_MAX = 0x1f
EV_CNT = (EV_MAX + 1)
