import socket
import struct
from math import sin, cos
from base import Base

BASE_PORT = 10000

class Robot(Base):
    '''
    A class that represents a robot with a position and an angle in the 2D plane.
    The position of the robot is updated by the Base object.
    '''
    def __init__(self, base = None, sock = None, port = BASE_PORT):
        '''
        Constructor. Creates a robot. If no parameters are given, the robot is
        at the origin and is facing in the positive x direction.
        '''
        Base.__init__(self, base, sock, port)
        self.angle = 0.0
    
    def __str__(self):
        '''
        Override the __str__ method.
        '''
        return 'Robot: (%f, %f), %f' % (self.x, self.y, self.angle)
    
    def rotate(self, angle):
        '''
        Rotate the robot. Positive angles are counter-clockwise.
        '''

