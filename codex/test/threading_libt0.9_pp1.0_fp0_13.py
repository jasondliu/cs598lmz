import threading
threading._DummyThread._Thread__stop = lambda x: 42
import time
import logger
import numpy as np
import Drive

#AutonomousFile constructor
#expects a filename to read from and an update period in seconds
def Auto2(filename, update_period, is_red_zone=False, print_errors=True, wait_for_start=True, use_gyro=None):

    drive = Drive.Drive()
    def Run():
        logger.log("Running Autonomous2")
        pieces = []
        piece = []
        mode = "step"
        index = 0
        file = open(filename + ".txt", "r")
        for line in file:
            if index >= 2 and (line == "\n" or line == ""):
                pieces += [piece]
                piece = []
                if index == 3:
                    mode = "auto"
            else:
                piece = line.split("\t")
