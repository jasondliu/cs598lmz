import gc, weakref
import logging

# Local imports
import adafruit_bus_device.i2c_device as i2c_device
from micropython import const

_LOGGER = logging.getLogger('adafruit_bno055')

# pylint: disable=bad-whitespace
# Internal constants:
_CHIP_ID                 = const(0xA0)

# Page id register definition
_PAGE_ID_ADDR            = const(0x07)

# PAGE0 REGISTER DEFINITION START
_CHIP_ID_ADDR            = const(0x00)
_ACCEL_REV_ID_ADDR       = const(0x01)
_MAG_REV_ID_ADDR         = const(0x02)
_GYRO_REV_ID_ADDR        = const(0x03)
_SW_REV_ID_LSB_ADDR      = const(0x04)
_SW_REV_ID_MSB_ADDR      = const(0x05)
_BL_REV_ID_AD
