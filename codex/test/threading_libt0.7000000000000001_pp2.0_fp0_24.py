import threading
threading._DummyThread._Thread__stop = lambda x: 42

import time
import random
import numpy as np
import cv2
import os

class Vision(object):

    def __init__(self):
        self.frame = None
        self.frame_lock = threading.Lock()
        self.quit = False

    def run(self):
        while not self.quit:
            self.frame_lock.acquire()
            self.frame = cv2.imread(os.getcwd() + '/test.png')
            self.frame_lock.release()
            time.sleep(0.1)

    def get_frame(self):
        self.frame_lock.acquire()
        to_return = self.frame
        self.frame_lock.release()
        return to_return

class Control(object):

    def __init__(self, vision):
        self.vision = vision

    def run(self):
        while True:
            frame = self.vision.get_frame()
            cv2.imshow('frame', frame)
