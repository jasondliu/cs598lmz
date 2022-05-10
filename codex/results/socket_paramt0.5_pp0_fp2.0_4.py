import socket
socket.if_indextoname(i)

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------

from netifaces import interfaces, ifaddresses, AF_LINK
iface = 'en0'
iface_mac = ifaddresses(iface)[AF_LINK][0]['addr']

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------

from netifaces import interfaces, ifaddresses, AF_INET
iface = 'en0'
iface_ip = ifaddresses(iface)[AF_INET][0]['addr']

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------

from netifaces import interfaces, ifaddresses, AF_INET
iface = 'en0'
iface_netmask = ifaddresses(iface)[AF_INET][0]['netmask']

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------

from netifaces import interfaces, ifaddresses, AF_INET
iface = 'en0'
iface_broadcast = ifaddresses(iface)[AF_INET][0]['broadcast']

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------


