import _struct as struct
import binascii as ba
import random as rdm
import sys
import time as tm

class MyZeroMQ:
    """
    Class to handle zmq connection and message passing
    """
    def __init__(self, port=5000, host='localhost'):
        self.port = port
        self.host = host
        self.context = zmq.Context()
        self.socket = context.socket(zmq.REQ)
        self.socket.connect("tcp://%s:%s" % (self.host, self.port))
        self.batchSize = 1000
        self.numBatch = 500

    def getNumBatch(self):
        return self.numBatch

    def setNumBatch(self, num):
        self.numBatch = num
        return

    def getBatchSize(self):
        return self.batchSize

    def setBatchSize(self, size):
        self.batchSize = size
        return

    def getHost(self):
        return self.host

