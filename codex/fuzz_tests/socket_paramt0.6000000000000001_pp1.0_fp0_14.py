import socket
socket.if_indextoname(index)

from scapy.all import *
from scapy.arch import *
from scapy.layers.inet import *
from scapy.layers.dot11 import *
from scapy.layers.eap import *
from scapy.layers.l2 import *
from scapy.layers.inet6 import *
from scapy.layers.dhcp6 import *

import sys
import getopt
import threading
import signal
import time
import os

import pcapy
from impacket.ImpactDecoder import RadioTapDecoder

def banner():
    print("""
    ##############################################################################
    #                                                                            #
    #         MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM       #
    #         MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM       #
    #         MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
