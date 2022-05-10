import socket
# Test socket.if_indextoname()
#print(socket.if_indextoname(1))

from scapy.all import *
import sys
from time import sleep

# Get the list of all interfaces on the system
ifaces = IFACES.dev_from_index
from scapy.data import ETH_P_ALL
#print(ifaces)

# Create a raw socket and bind it to the public interface
def main():
    rawSocket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_ALL))
    rawSocket.bind((ifaces[1], 0))
    print(rawSocket.recvfrom(65536))

