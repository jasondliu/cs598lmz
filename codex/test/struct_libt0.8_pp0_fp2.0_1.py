import _struct
# the struct module helps to write c code in python in an easy way
import sys

import psutil
# psutil is a process and system utilities module for Python
# import the process class

from winappdbg import Process
# WinAppDbg is a package that allows to debug native Windows applications
# import the Process object

from _winapi import INFINITE

## Custom imports
from core.advancedDebugger.exceptionClass import *
from utils import *

OFFSET_CONTROL_INSTR = 0xE8
OFFSET_CONTROL_EXCEPTION = 0xEC
OFFSET_CONTROL_FIRST_CHANCE = 0xF0
OFFSET_CONTROL_UNLOAD_MODULE = 0xF4
OFFSET_CONTROL_SECOND_CHANCE = 0xF8
OFFSET_CONTROL_OUTPUT_DEBUG_STRING = 0xFC
OFFSET_CONTROL_THREAD_CREATED = 0x100
OFFSET_CONTROL_EXIT_PROCESS = 0x104
OFFSET_CONTR
