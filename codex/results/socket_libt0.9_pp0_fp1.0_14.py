import socket
import argparse
import threading
import re
import time
import Queue
import sys
from scapy.all import *
sys.path.insert(0, './src')
import ssdp
from scapy.all import Ether, ARP, get_if_hwaddr, getmacbyip, srp
from scapy.arch import get_if_list
from enum import Enum

#######################################
# Function: Enum of device types. 
#######################################
class DeviceTypes(Enum):
    Printer = 'Printer'
    Scanner = 'Scanner'
    Projector = 'Projector'

#######################################
# Function: A custom ssl_shake to be used with scapy. 
#######################################
class my_ssl_shake(ssl_handshake):
    name = "TLS Handshake"
    fields_desc = [ ByteEnumField("type", 20, {20: "server_hello", 22: "certificate"}),
                    XStrLenField("data", "", length_from = lambda pkt:pkt.length) ]

################################
