import select
import socket
import sys
import time
import traceback

import numpy as np
import pygame

from pydynamixel import dynamixel, registers, util

class Servo(object):
    def __init__(self, id, name, init_angle=0.0, min_angle=0.0, max_angle=300.0,
                 min_pwm=0, max_pwm=1023):
        self.id = id
        self.name = name
        self.init_angle = init_angle
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.min_pwm = min_pwm
        self.max_pwm = max_pwm
        self.angle = init_angle
        self.pwm = self.angle_to_pwm(init_angle)

    def angle_to_pwm(self, angle):
        if angle < self.min_angle or angle > self.max_angle:
            raise ValueError("Angle %f out of range [%f, %f]"
