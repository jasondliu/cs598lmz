import socket
import logging
import sys

logger = logging.getLogger(__name__)

class InetAddress:
    """
    Utility class representing an IP address and port
    """
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def __eq__(self, other):
        return self.ip == other.ip and self.port == other.port

    def __hash__(self):
        return hash(self.ip) ^ hash(self.port)

    def __str__(self):
        return "%s:%s" % (self.ip, self.port)

    def __repr__(self):
        return "InetAddress(%s)" % self

    def __ne__(self, other):
        return not self.__eq__(other)

class TCPSocket:
    """
    Utility class representing a TCP connection to another node.
    """
    def __init__(self, ip, port):
        self.address = InetAddress(ip, port)
