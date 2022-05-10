import socket
import struct
import binascii


# BSSID MAC structure
class MAC(object):
    def __init__(self, mac):
        self.addr = mac

    def d(self):
        return binascii.unhexlify(self.addr.replace(':', ''))

    def hex(self):
        return self.addr.replace(':', '')

    def raw(self):
        return int(self.addr.replace(':', ''), 16)


# Client addr structure
class ADDRA(object):
    def __init__(self, addr, bssid, power):
        self.addr = addr
        self.bssid = bssid
        self.power = power


# net nugget for nugget flow
class Nugget:

    def __init__(self, post_url=None, is_headless=True):
        self.__interface = None
        self.__channel = None
        self.__bssid = None
        self.__post = post_url
        self.__headless = is_
