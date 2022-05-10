import select
import sys
import threading
import time

import usb

DEVICE_VID = 0x0483
DEVICE_PID = 0x5740

# Based on https://github.com/firepick1/firepick-node/blob/master/src/firenode.c
# usb-device 0x0483:0x5740

class FireNode(object):
    def __init__(self):
        self.device = None
        self.interface = None
        self.endpoint = None
        self.handle = None
        self.callbacks = {}
        self.thread = None

    def __del__(self):
        if self.thread is not None:
            self.thread.join()
            self.thread = None
        if self.handle is not None:
            self.handle.close()
            self.handle = None

    def find_device(self):

        self.device = usb.core.find(idVendor=DEVICE_VID, idProduct=DEVICE_PID)
        if self.device is None:
            raise Exception("device
