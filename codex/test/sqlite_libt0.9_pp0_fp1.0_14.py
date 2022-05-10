import ctypes
import ctypes.util
import threading
import sqlite3

import PyLuaTblParser
from pylibftdi.driver import DeviceNotFound
from pylibftdi import BitBangDevice
from pylibftdi.driver import AutoDevice
from pylibftdi import __version__ as pylibftdi_version
from USBBitBangReg import USBBitBangReg


#
# Module level definitions
#

RT_PAGE_WRITETHROUGH = 0x80000000
RT_PAGE_NO_CACHE     = 0x20000000
RT_PAGE_READWRITE    = 0x04

PAGE_SIZE            = 0x1000

MICROPY_RAM_BASE     = 32 * 1024 * 1024

BLOCK_SIZE           = 16 * 1024

#
# Some amount of RAM will be reserved as a hardware stack. If interrupt routines
# use SP at the time of interrupt this is a convenient value to make sure MP
# stack does not over reach into hardware stack.
#
HARDWARE_STACK_SIZE  = 16 * 1024

MICROPY_RAM_SIZE     = 8 * 1024 * 1024

