import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os
import time
import re
import math

class CPAntiDebug(object):
    """Anti debugging class (Windows)"""
    pass


class CPAntiDump(object):
    """Anti-dump class (Windows)"""
    pass


class CPAntiVM(object):
    """Anti-VM class (Windows) - based on @hasherezade's work"""
    _list_smi_1 = [
        'ROOT\\WMI:Msvm_ComputerSystem',
    ]

    _list_smi_2 = [
        'ROOT\\WMI:Msvm_ComputerSystem',
        'ROOT\\WMI:Msvm_OperatingSystem',
    ]

    _list_smi_3 = [
        'ROOT\\CIMV2:Win32_ComputerSystem',
        'ROOT\\CIMV2:Win32_OperatingSystem',
    ]

    _list_rare_keys = [
        'HARDWARE\\DESCRIPTION\\System\\FirmwareTable',
        'HARDWARE\\
