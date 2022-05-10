import socket
socket.if_indextoname(socket.if_nametoindex("eth0"))

import netifaces as ni
ni.ifaddresses('eth0')
ni.interfaces()
sep = "-" * 70

# This function just prints out basic information about
# each interface.
def print_nic_info():
    for interface in ni.interfaces():
        print "*** Interface %s ***" % interface

        # MAC address
        mac = ni.ifaddresses(interface)[ni.AF_LINK]
        mac = mac[0]['addr']
        print "  MAC address:       %s" % mac

        # IP address
        ip = ni.ifaddresses(interface)[ni.AF_INET]
        ip = ip[0]['addr']
        print "  IP address:        %s" % ip

        # Netmask
        netmask = ni.ifaddresses(interface)[ni.AF_INET]
        netmask = netmask[0]['netmask']
        print "  Netmask:           %s" % netmask

        # Packet count
        pkts_in =
