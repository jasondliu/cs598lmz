import _struct
from pymavlink import mavutil
from pymavlink.mavextra import *
from pymavlink.rotmat import Vector3, Matrix3
from pymavlink.mavwp import MAVWP
from pymavlink import mavwp, mavparm


class mavfile(object):
    '''a generic mavlink port'''
    def __init__(self, device, input=False, baud=115200, autoreconnect=False, source_system=255, source_component=0,robust_parsing=True):
        '''open a mavlink serial/udp port'''
        self.robust_parsing = robust_parsing
        self.device = device
        self.port = serial.Serial(device, baud, timeout=0,
                                  dsrdtr=False, rtscts=False, xonxoff=False)
        self.port.flushInput()
        self.port.flushOutput()
        self.last_seq = 0
