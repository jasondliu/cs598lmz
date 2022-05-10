import mmap
import struct
import os
import subprocess
import sys
import re
import traceback
from intelhex import IntelHex
from intelhex import HexRecordError
from intelhex import HexReaderError
import argparse

# iHex & ELF file types
iHex     = 'IHEX'
ELF      = 'ELF'

# No error
NO_ERROR              =  0
# Hex record errors
IHEX_INVALID_CHKSUM   = -1
# Programmer errors
BAD_PID               = -2
UNKNOWN_CHIP          = -3
# Mapping file errors
BAD_MAP_LINE          = -4

# Flash programming errors
CHIP_ERASE_FAILED     = -5
FLASH_WRITE_FAILED    = -6
READ_VERIFY_FAILED    = -7

# Flash programming parameters
# These are in this file to make it easier to tune
# The default values will work for AT91SAM7X256

# Number of bytes to write at a time
# This needs to be large enough to prevent
