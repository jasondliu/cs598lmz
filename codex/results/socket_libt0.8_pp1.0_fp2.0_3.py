import socket
import struct

class netlink_object(object):
    """Generic class for all netlink objects"""
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.netlink_socket = None

    def set_netlink_socket(self, netlink_socket):
        self.netlink_socket = netlink_socket

    @abc.abstractmethod
    def receive_message(self):
        pass

    @abc.abstractmethod
    def send_message(self):
        pass

    @abc.abstractmethod
    def parse_netlink_message(self, msg):
        pass

class netlink_socket(object):
    """Generic class for netlink socket"""
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.netlink_socket = None
        self.netlink_object = []
        self.group_id = 0
        self.family_id = 0
        self.open()

    def add_netlink_object(self, obj):
        """Add
