import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("c:/info.db")
import time

class SNMP:
    # client
    # net-snmp version 5.6
    # snmpget -v2c -c public 192.168.10.1 iso.3.6.1.4.1.637.61.1.3.1.1.1.0
    
    def __init__(self, addr, community, version='2'):
        self.addr = addr
        self.community = community
        self.version = version
        self.flag = False
        self.lock = threading.Lock()
    
    class VarBind(ctypes.Structure):
        _fields_ = [('name', ctypes.c_char_p),
                    ('value', ctypes.c_char_p)]
    
    class SNMP_PDU(ctypes.Structure):
        _fields_ = [('command', ctypes.c_int),
                    ('errstat', ctypes.c_int),
                    ('errindex', ctypes.c_int),
                    ('bindings', ctypes.PO
