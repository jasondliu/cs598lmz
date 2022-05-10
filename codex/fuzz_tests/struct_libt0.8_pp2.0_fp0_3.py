import _struct

import errno
import logging
import time

class SocketTimeoutReconnect(Exception):
    pass

class Socket:
    
    def __init__(self, sock_type="", sock_domain=socket.AF_INET, sock_proto=socket.IPPROTO_TCP):
        self.__s = None
        self.__s_type = sock_type
        self.__s_domain = sock_domain
        self.__s_proto = sock_proto
        self.__s_connected = False
        self.__s_timeout = 5
        self.__s_default_timeout = self.__s_timeout
        self.logger = logging.getLogger()
    
    def __del__(self):
        if self.__s is not None:
            self.__s.close()
        
    def connect(self, addr, port):
        if not self.__s_connected:
            self.create()
            self.__s.connect((addr, port))
            self.__s_connected = True
        return self
