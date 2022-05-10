import mmap
import struct
import sys
import time

# For Python 2.x and 3.x compatibility: 3.x has not raw_input builtin
# otherwise 2.x's input builtin function is too "smart"
if sys.version_info.major < 3:
    input_function = raw_input
else:
    input_function = input


# Global constants
# I2C Address of the device
I2C_ADDR = 0x48

# Register addresses
REG_INPUT = 0x00
REG_CONF = 0x01
REG_LOW_THRESH = 0x02
REG_HIGH_THRESH = 0x03

# Config register values
CONF_SD = 0x0100
CONF_COMP_QUE = 0b11
CONF_COMP_LAT = 0x0800
CONF_COMP_POL = 0x0400
CONF_COMP_MODE = 0x0100
CONF_DR = 0b111
CONF_TM = 0x0080
CONF_OS = 0x0020

# Conversion delay
