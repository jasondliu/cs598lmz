import mmap
import struct
import sys
import time

#
# HARDWARE CONSTANTS
#

#
# I/O PORTS
#

# I/O port for the 8-bit data bus
DATA_BUS = 0xFF00

# I/O port for the 8-bit address bus
ADDR_BUS = 0xFF01

# I/O port for the 8-bit control bus
CTRL_BUS = 0xFF02

# I/O port for the 8-bit interrupt bus
INT_BUS = 0xFF03

# I/O port for the 8-bit interrupt enable bus
INT_ENABLE_BUS = 0xFF04

# I/O port for the 8-bit interrupt acknowledge bus
INT_ACK_BUS = 0xFF05

# I/O port for the 8-bit interrupt pending bus
INT_PENDING_BUS = 0xFF06

# I/O port for the 8-bit interrupt reset bus
INT_RESET_BUS = 0xFF07

# I/O port for the 8-bit interrupt reset bus
