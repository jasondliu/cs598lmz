import socket
import os
import sys
import random
from struct import unpack, pack
import traceback
import zlib
import errno
import threading
import re

from netaddr import IPAddress, IPNetwork
from threading import Lock
from multiprocessing import Queue, cpu_count
from scapy.all import conf
from scapy.all import sendp, send, IP, TCP, send, fragment
#from scapy.all.sendrecv import AsyncSniffer

from burst_traceroute import constants
from burst_traceroute.traceroute_packet import \
    TracerouteReplyPacket, TracerouteProbePacket
from burst_traceroute.common import logger
from burst_traceroute.common import utils
from burst_traceroute.config import options

conf.verb = 0

class TCPSender(object):
    """
    Used to send packets.
    Randomly assign a local port to be the source port.
    And using the same local IP of the interface for outgoing.
    """

    def __init__(self, **kw
