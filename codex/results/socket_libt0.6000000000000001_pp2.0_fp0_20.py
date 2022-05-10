import socket
import struct
import time
import threading

from six.moves import queue

from scapy.all import Ether, IP, UDP, BOOTP, DHCP, DNS, DNSQR, DNSRR, TCP
from scapy.all import ARP, conf, wrpcap, rdpcap
from scapy.layers.inet import IP_PROTOS, TCP_SERVICES, UDP_SERVICES
from scapy.config import conf

from . import utils
from . import dnsutils
from . import tls
from . import udp
from . import tcp
from . import arp
from . import dhcp
from . import logger
from . import constants
from . import pcap
from . import ethernet
from . import packet

class Dataplane(object):
    """
    Class to receive and send packets from a dataplane interface.
    """
    def __init__(self, iface):
        """
        Initialize the dataplane

        :param iface: interface name to bind to
        :return: None
        """
        self.logger = logger.getLogger
