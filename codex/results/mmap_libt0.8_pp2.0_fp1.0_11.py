import mmap
import struct
import socket
import pprint
import subprocess
from optparse import OptionParser, OptionValueError
import os
import re
from scapy.all import *
from collections import defaultdict

from scapy.layers.inet import IP, TCP
from scapy.all import * 
import sys
from collections import OrderedDict


formats = {'name':{'size':50, 'format':'%s'},
           'num_pkts':{'size':10, 'format':'%d'},
           'total_bytes':{'size':10, 'format':'%d'},
           'tcp_bytes':{'size':10, 'format':'%d'},
           'udp_bytes':{'size':10, 'format':'%d'},
           'icmp_bytes':{'size':10, 'format':'%d'},
           'other_bytes':{'size':10, 'format':'%d'},
           'total_pkts':{'size':10, 'format':'%d'
