import socket
# Test socket.if_indextoname
#
# if_indextoname() takes an interface index, and returns the name of the
# interface.
#
# Author: Giuseppe Ottaviano
#
# $Id: if_indextoname.py,v 1.1 2004/07/19 09:58:20 giuseppe Exp $

from socket import *
from socket_helper import *

s = socket(AF_INET, SOCK_DGRAM)

for i in range(0, len(if_names)):
    ifname = if_indextoname(i)
