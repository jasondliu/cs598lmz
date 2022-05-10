import socket
# Test socket.if_indextoname() and socket.if_nametoindex()
#
# To pass in test config, create a local override file called
# test/test_socket.py and override socket_ifname as below
#
# socket_ifname = {
#     "Linux": "lo",
#     "FreeBSD": "lo0"
# }
#
# To find a suitable interface for testing, try the following commands:
#
# Linux:    ip a | grep 'state UP' -A2 | tail -n1 | cut -d ':' -f2 | tr -d ' '
# FreeBSD:  'sysctl net.link | grep "ver1:"'

import os
import platform
import sys
import unittest

