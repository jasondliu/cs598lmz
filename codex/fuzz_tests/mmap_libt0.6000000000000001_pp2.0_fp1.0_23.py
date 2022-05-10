import mmap
import socket
import sys
import codecs
import datetime
import os
import re
import signal
import time
import threading

from dns.rdtypes.ANY.CNAME import CNAME
from dns.rdtypes.ANY.NS import NS
from dns.rdtypes.ANY.SOA import SOA
from dns.rdtypes.ANY.SRV import SRV
from dns.rdtypes.ANY.TXT import TXT
from dns.rdtypes.IN.A import A
from dns.rdtypes.IN.AAAA import AAAA
from dns.rdtypes.IN.HINFO import HINFO
from dns.rdtypes.IN.MX import MX
from dns.rdtypes.IN.NAPTR import NAPTR
from dns.rdtypes.IN.PTR import PTR
from dns.rdtypes.IN.RP import RP
from dns.rdtypes.IN.SIG import SIG
from dns.rdtypes.IN.SPF import SPF
from dns.rdtypes.IN.TKEY import TKEY
from dns.rdtypes
