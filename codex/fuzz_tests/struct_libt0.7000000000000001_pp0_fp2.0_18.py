import _struct
from array import array
from fcntl import ioctl

import errno
import time

# ioctl constants from <linux/i2c-dev.h>
I2C_SLAVE = 0x703
I2C_SMBUS = 0x720
I2C_SMBUS_READ = 1
I2C_SMBUS_WRITE = 0
I2C_SMBUS_QUICK = 0
I2C_SMBUS_BYTE = 1
I2C_SMBUS_BYTE_DATA = 2
I2C_SMBUS_WORD_DATA = 3
I2C_SMBUS_PROC_CALL = 4
I2C_SMBUS_BLOCK_DATA = 5
I2C_SMBUS_I2C_BLOCK_BROKEN = 6
I2C_SMBUS_BLOCK_PROC_CALL = 7
I2C_SMBUS_I2C_BLOCK_DATA = 8

# This is a simple class for reading and writing
# I2C registers on a
