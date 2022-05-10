import socket
# Test socket.if_indextoname()

import os
import sys
import time
import struct
from subprocess import call

from scapy.all import sniff, sendp, IP, TCP, UDP, Ether, RandIP, RandMAC
from scapy.all import get_if_hwaddr
from scapy.all import get_if_addr

from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Intf

from argparse import ArgumentParser

from util.util import *

parser = ArgumentParser("Monitoring Agent")
parser.add_argument('--controller', '-c',
                    dest="controller",
                    action="store",
                    type=str,
                    help="Hostname or IP of the remote controller")
parser.add_argument('--port', '-p',
                    dest="port",
                    action="store",
                    type=int,
                    help="Port of the remote controller")
parser.add_argument('--interface', '-i',
                    dest="interface
