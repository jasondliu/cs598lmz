import _struct
import time
import random
import argparse
import os
import sys

try:
    import _pcap
except ImportError:
    raise ImportError("pypcap module is not installed")


def _parse_mac(mac_string):
    """
    Parse a MAC address string into its byte representation.
    """
    if len(mac_string) != 17:
        raise ValueError("MAC address must be 17 bytes long")
    try:
        return struct.unpack('!BBBBBB', binascii.unhexlify(mac_string.replace(':', '')))
    except (TypeError, binascii.Error):
        raise ValueError("%s is not a valid MAC address" % mac_string)


def _parse_ip(ip_string):
    """
    Parse an IPv4 address string into its byte representation.
    """
    try:
        return socket.inet_aton(ip_string)
    except socket.error:
        raise ValueError("%s is not a valid IP address" % ip_string)


def _parse_
