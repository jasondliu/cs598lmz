import socket
import sys

from PIL import Image
from PIL.ImageOps import fit
from io import BytesIO

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QPixmap
from PyQt4.QtCore import QThread

from . import message_dialog
from . import server_config
from . import client


class CameraStreamHandler(QThread):
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.parent = parent

        self.running = True
        self.client = client.Client(server_config.SERVER_IP, server_config.SERVER_PORT)

        self.width = self.parent.label.width()
        self.height = self.parent.label.height()

        self.image = None

    def run(self):
        while self.running:
            self.image = self.client.get_frame()

            # self.image = cv2.imread('C:/Users/Kuba/Downloads/
