import socket
# Test socket.if_indextoname('192.168.1.1')

from time import time
import sys
from struct import pack
from struct import unpack
from struct import calcsize
from struct import pack_into
from struct import unpack_from
from struct import error
import re
import os
import signal
from signal import SIGINT, SIG_IGN

from pyroute2.netlink.rtnl import RTM_NEWLINK
from pyroute2.netlink.rtnl import RTM_DELLINK
from pyroute2.netlink.rtnl import RTM_NEWADDR
from pyroute2.netlink.rtnl import RTM_DELADDR
from pyroute2.netlink.rtnl import RTM_NEWROUTE
from pyroute2.netlink.rtnl import RTM_DELROUTE
from pyroute2.netlink.rtnl import RTM_NEWNEIGH
from pyroute2.netlink.rtnl import RTM_DELNEIGH
from pyroute2.netlink.rtnl import RTM_NEWQDISC
