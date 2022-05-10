import socket
# Test socket.if_indextoname()
import sys
import time

import pytest
import six

from pyroute2 import IPRoute
from pyroute2.netlink import NLM_F_REQUEST
from pyroute2.netlink import NLM_F_DUMP
from pyroute2.netlink import NLM_F_EXCL
from pyroute2.netlink import NLM_F_CREATE
from pyroute2.netlink import NLM_F_ACK
from pyroute2.netlink import NLMSG_DONE
from pyroute2.netlink import NLMSG_ERROR
from pyroute2.netlink import NLMSG_OVERRUN
from pyroute2.netlink import NLM_F_ACK
from pyroute2.netlink import NLM_F_MULTI
from pyroute2.netlink import NLM_F_ATOMIC
from pyroute2.netlink import NLM_F_ECHO
from pyroute2.netlink import NLM_F_REPLACE
