import mmap
import numpy as np
import os
import random
import struct
import sys
import time
import cv2
from multiprocessing import Process, Pipe
import torchvision
import carla


class Timer(object):
    def __init__(self):
        self.reset()

    def tic(self):
        # using time.time instead of time.clock because time time.clock
        # does not normalize for multithreading
        self.start_time = time.time()

    def toc(self, average=True):
        self.diff = time.time() - self.start_time
        self.total_time += self.diff
        self.calls += 1
        self.average_time = self.total_time / self.calls
        if average:
            return self.average_time
        else:
            return self.diff
    
    def reset(self):
        self.total_time = 0.
        self.calls = 0
        self.birth = time.time()

    def fulltoc(self):
        return time.time()
