import _struct
import ctypes
from ctypes import byref
from functools import reduce
import os
import pathlib
import platform
import random
import sys
import time
from util import *

# Constants
# All tokens that can be passed to RtlAdjustPrivilege()
RLT_ADJUST_PRIVILEGE_TOKEN_VALUES = [3, 4, 5, 6, 7, 8, 9, 10,
                                     11, 12, 13, 14, 15, 16, 17]
# All tokens that can be passed to NtAdjustPrivilege()
NT_ADJUST_PRIVILEGE_TOKEN_VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# Tokens used while using a process token
CURRENT_PROCESS_TOKEN_VALUES = RLT_ADJUST_PRIVILEGE_TOKEN_VALUES
# Tokens used while using a thread token
CURRENT_THREAD_TOKEN_VALUES = NT_ADJUST_PRIVILEGE_TOKEN_VALUES
CURRENT_TOKEN
