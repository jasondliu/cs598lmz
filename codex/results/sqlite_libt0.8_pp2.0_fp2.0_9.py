import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import time

import numpy as np

#import pdb


class DataStructure(object):
    """docstring for DataStructure"""
    def __init__(self,):
        super(DataStructure, self).__init__()

        self.arglist = []
        self.arglist.append('1')
        self.arglist.append('2')


    def get_arglist(self):
        return self.arglist


class DataProcess(object):

    def __init__(self):
        self.data = 0
        self.arglist = None

    def process(self, data, arglist):
        self.data = data
        self.arglist = arglist
        return data


class ProcessThread(threading.Thread):
    """docstring for ProcessThread"""
    def __init__(self):
        super(ProcessThread, self).__init__()

        self.data = None
        self.arglist = None

    def run(self):
        self.process()

    def process(self):
        #print
