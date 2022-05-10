from lzma import LZMADecompressor
LZMADecompressor.flush = lambda self, x: self.flush_buffer()
from lxml import etree
from socket import socket, AF_INET, SOCK_DGRAM
from struct import unpack
from sys import argv
from time import sleep, struct_time
from uuid import UUID
from zlib import decompress
#}

#{ definitions
STX = b'\x1e'
ETX = b'\x03'
NUL = b'\x00'
ACK = b'\x06'
DC2 = b'\x12'
CAN = b'\x18'

SERVO_IMU = 0x0
SERVO_SENSORS = 0x1

IMU_ANGLE_X = 0x2
IMU_ANGLE_Y = 0x3
IMU_ANGLE_Z = 0x4
IMU_ACCEL_X = 0x5
IMU_ACCEL_Y = 0x6
IMU_ACCEL_Z = 0x7
IMU_MAGNET_X = 0x8
IMU_MAGNET_Y =
