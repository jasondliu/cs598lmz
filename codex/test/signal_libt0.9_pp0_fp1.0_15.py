import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import argparse
import os
import logging

from PyQt4 import QtGui, QtCore

import picamera


class RaspiCam(QtCore.QThread):
    newFrame = QtCore.Signal(QtGui.QImage)

    def __init__(self):
        QtCore.QThread.__init__(self)
        self.raspiLogo = QtGui.QImage("raspicam.png")
        self.runFlag = False
        self.raspiCam = picamera.PiCamera()
        self.raspiCam.resolution = (640, 480)
        self.raspiCam.framerate = 24
        time.sleep(2)
        self.raspiCam.iso = 800
        time.sleep(2)
        self.raspiCam.shutter_speed = 6000000
        time.sleep(2)
        self.raspiCam.awb_mode = 'off'
        self.r
