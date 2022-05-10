import socket
import struct
import time

import numpy as np

from PyQt5.QtCore import QObject, pyqtSignal

from . import udp_server

class ZaberData(QObject):
    """
    Class for handling Zaber data
    """

    # signal for updating the plot
    update_signal = pyqtSignal()

    def __init__(self):
        QObject.__init__(self)

        self.data = np.zeros(1)
        self.x_data = np.zeros(1)

        self.axis = 0
        self.position = 0
        self.speed = 0
        self.acceleration = 0
        self.stop_code = 0

    def update(self, data):
        """
        Update data
        """

        self.data = np.append(self.data, data)
        self.data = self.data[-200:]
        self.x_data = np.linspace(0, len(self.data), len(self.data))
        self.update_signal
