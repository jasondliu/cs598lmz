import types
types.ModuleType

import sys
#sys.path.append("/home/pi/git/quick2wire-python-api")
sys.path.append("/home/pi/git/quick2wire-python-api/quick2wire")
import quick2wire.i2c as i2c
import math

#set up the i2c bus and pins
i2c_bus_number=1
i2c_address=0x68

bus = i2c.I2CMaster(i2c_bus_number)

#set up the mpu6050
MPU6050_RA_XG_OFFS_TC=0x00
MPU6050_RA_YG_OFFS_TC=0x01
MPU6050_RA_ZG_OFFS_TC=0x02
MPU6050_RA_X_FINE_GAIN=0x03
MPU6050_RA_Y_FINE_GAIN=0x04
MPU6050_RA_Z_FINE_GAIN=0x05
MPU6050_RA_XA
