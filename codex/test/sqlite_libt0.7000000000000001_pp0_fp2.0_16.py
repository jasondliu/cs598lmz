import ctypes
import ctypes.util
import threading
import sqlite3
import socket
import time

class Tox(object):
    def __init__(self, ipv6enabled=False, proxytype=None, proxyhost=None, proxyport=None,
                 udpdisabled=False, localport=0, nospam=0, publickey=None,
                 secretkey=None, userstatus=None, name=None, statusmessage=None):
        """
        create a new Tox instance.
        ipv6enabled - enable ipv6 support
        proxytype - type of proxy to use, one of TOX_PROXY_TYPE_SOCKS*
        proxyhost - proxy host or ip address
        proxyport - proxy port
        udpdisabled - disable udp support
        localport - use a specific local port
        nospam - nospam value
        publickey - public key
        secretkey - secret key
        userstatus - user status
        name - name
        statusmessage - status message
        """
        self._lock = threading.Lock()
