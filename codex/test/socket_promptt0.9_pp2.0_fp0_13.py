import socket
# Test socket.if_indextoname
from socket import gethostname
import os
from binascii import hexlify
import json
from scapy.all import *
from scapy.utils import PcapReader, PcapWriter, rdpcap
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, TCP
from scapy.layers.inet import UDP
from scapy.layers.dns import DNSQR, DNSRR, DNS
from scapy.layers.http import HTTP, HTTPRequest, HTTPResponse
from io import BytesIO
from datetime import datetime
from collections import OrderedDict
from time import time
from struct import unpack
from struct import pack
from socket import inet_ntoa
from copy import copy
import hashlib

# date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S.%f")[:-3]

TIME_MINUTE = 15


def __make_timestamp(tstamp):
    tstamp = int(tstamp)
    sec
