import ctypes
import ctypes.util
import threading
import sqlite3
import struct
import signal
import sys
import traceback
import os

from elftools.elf.elffile import ELFFile
from elftools.elf.sections import SymbolTableSection
from elftools.elf.descriptions import (
    describe_symbol_type, describe_symbol_shndx,
    describe_p_type, describe_p_flags,
)

class SystemTapError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class SystemTap:
    """SystemTap interface"""
    def __init__(self, filename, process):
        self.filename = filename
        self.process = process
        self.process.systemtap = self

        # Setup signal handler to unload on SIGUSR1
        signal.signal(signal.SIGUSR1, self.signal_handler)

        # Determine filename of tpf_process_executable
