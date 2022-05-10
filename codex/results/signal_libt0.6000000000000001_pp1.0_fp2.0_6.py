import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import numpy as np
import random
import argparse
import os
import time
import sys
import math
import matplotlib.pyplot as plt
import pygame
import pypot.robot
import pypot.dynamixel
import pypot.robot.config
from pypot.dynamixel.controller import DxlController

from pybrain.rl.environments.environment import Environment

#from pypot.primitive.utils import Sinus
from sinus import Sinus

class SinusEnvironment(Environment):
    """ A simple sinusoid environment.
    """
    def __init__(self, motor_names, frequency=1, amplitude=30, offset=0):
        self.motor_names = motor_names
        self.frequency = frequency
        self.amplitude = amplitude
        self.offset = offset
        self.time = 0
        self.values = {}

    def getSensors(self):
        """ Returns the current sensor values. """
