import socket
socket.if_indextoname('0x5')

'''

import argparse
import os
import socket
import struct
import sys
import time


__version__ = '0.3.3'


def parse_args(argv=None):
    """Parse command-line arguments.

    Args:
        argv (list, optional): An argument list to parse. Default is the result
            of sys.argv[1:].

    Returns:
        Namespace: The collection of parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="Listens to wired or wireless traffic and determines "
                    "whether the network is truly idle. Unlike some tools "
                    "that only check to see if DHCP packets are available, "
                    "this tool requires proof that at least one device is "
                    "actively sending traffic over the network. This means "
                    "that idle neighbors do not influence the result. Also, "
                    "this tool can operate when IPv6 is enabled, since it "
                    "simply relies on which MAC address sent the traffic.")
    parser.add_argument('-i', '--
