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

    def run(self):
        print "Starting " + self.name
        iface = self.name
        sniff(iface=iface, prn=self.packet_callback, store=0)
        print "Exiting " + self.name

    def packet_callback(self, packet):
        print packet.summary()

#-------------------
# Main
#-------------------

if __name__ == "__main__":
    print "Running Threads"

    # Create new threads
    thread1 = Sniffer(1,
