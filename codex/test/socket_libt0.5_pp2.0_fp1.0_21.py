import socket
import os
import sys
import subprocess
import time
import threading
from scapy.all import *

#-------------------
# Global variables
#-------------------

#-------------------
# Global functions
#-------------------

#-------------------
# Class definition
#-------------------

class Sniffer(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

