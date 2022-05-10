import weakref
import threading
import time
import Queue
import os
import logging
import numpy as np

logger = logging.getLogger(__name__)

class GetDataThread(threading.Thread):
    '''
    Thread for getting the data from the device
    '''
    def __init__(self, device, data_queue, event):
        threading.Thread.__init__(self)
        self.device = device
        self.data_queue = data_queue
        self.event = event
        self.daemon = True

    def run(self):
        while not self.event.is_set():
            try:
                data = self.device.get_data(n=1, timeout=0.5)
            except Exception:
                logger.exception('Could not get data from device')
            else:
                if data:
                    self.data_queue.put(data)
                    self.event.wait(0.01)

class Device(object):
    def __init__(self, name, n_channels, stream, device_
