import socket
socket.if_indextoname(3)

#
# Example 5.11
#

import socket
socket.if_nameindex()

#
# Example 5.12
#

import socket
socket.if_nametoindex('lo')

#
# Example 5.13
#

import socket
socket.gethostbyname('localhost')

#
# Example 5.14
#

import socket
socket.gethostbyname_ex('localhost')

#
# Example 5.15
#

import socket
socket.gethostbyaddr('127.0.0.1')

#
# Example 5.16
#

import socket
socket.gethostbyname_ex('www.python.org')

#
# Example 5.17
#

import socket
socket.getnameinfo(('127.0.0.1', 80), 0)

#
# Example 5.18
#

import socket
socket.getnameinfo(('127.0.0.1', 80), socket.NI_NUMERICHOST)

#
# Example 5.19
#


