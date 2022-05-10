import socket
# Test socket.if_indextoname to see if it is present
try:
    socket.if_indextoname(1)
except AttributeError:
    socket.if_indextoname = None

import struct
import subprocess
import sys
import time
import threading

from pyroute2 import config
from pyroute2.common import uifname
from pyroute2.ipdb.exceptions import CommitException
from pyroute2.netlink import nla
from pyroute2.netlink import NLM_F_REQUEST
from pyroute2.netlink import NLM_F_MULTI
from pyroute2.netlink import NLM_F_ACK
from pyroute2.netlink import NLM_F_DUMP
from pyroute2.netlink import NLM_F_CREATE
from pyroute2.netlink import NLM_F_EXCL
from pyroute2.netlink import NLM_F_APPEND
from pyroute2.netlink import NLMSG_ERROR
from pyroute2.netlink import NLMSG_D
