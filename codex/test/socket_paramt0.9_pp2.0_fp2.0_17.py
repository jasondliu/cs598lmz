import socket
socket.if_indextoname(16)

try:
    import netifaces
except ImportError:
    netifaces = None

from twisted.trial import unittest
from twisted.internet import defer
from ooni import errors as e
from ooni.utils.net import (isPrivateIP, isIPAddress, isIPv8Address,
                            getMajorIPBlock, getLocalIPv6, getLocalIP)
from ooni.utils import log

log.start()

