import socket
# Test socket.if_indextoname()
import sys
# For getting command line arguments

def main ():

    # Get the interface name from the command line, e.g. "en1".
    if len(sys.argv) < 2:
        print("Provide an interface name as argument, e.g. en1")
        exit(1)
    ifn = sys.argv[1]

    # Create a raw socket.
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

    # Bind the socket to the port and interface.
    s.bind((ifn, 1))

    # Look up and convert the interface index to the interface name
    ifIdx = socket.if_nametoindex(ifn)
    ifName = socket.if_indextoname(ifIdx)

    print("Bind socket to interface %s using index %d." % (ifName, ifIdx))
    print("Listening for ICMP packets...")

    # Receive ICMP packets forever.
