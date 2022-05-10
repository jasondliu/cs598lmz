import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
from test import support
from socket import error
from socket import if_indextoname
from socket import if_nametoindex
from socket import AF_INET
from socket import AF_INET6
from socket import INADDR_ANY
from socket import INADDR_LOOPBACK
from socket import INADDR_BROADCAST
from socket import inet_pton
from socket import inet_ntop
from socket import getaddrinfo
from socket import getnameinfo
from socket import gethostbyname
from socket import gethostbyname_ex
from socket import gethostbyaddr
from socket import gethostname
from socket import getfqdn
from socket import gaierror
from socket import has_ipv6
from socket import herror
from socket import AI_PASSIVE
from socket import NI_NUMERICHOST
from socket import NI_NUMERICSERV
from socket import NI_NOFQDN
from socket import NI_NAMEREQD
from socket import NI_DGRAM
from socket import NI_MAXHOST
from socket
