import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('C:\Python27\patstat2015b.sqlite')
patstatConnection = sqlite3.connect('C:\Python27\patstat2015b.sqlite')
patstatConnection.row_factory = sqlite3.Row

patstatCursor = patstatConnection.cursor()

patstatReadCursor = patstatConnection.cursor()
patstatReadCursor.row_factory = sqlite3.Row

patstatUpdateCursor = patstatConnection.cursor()

def unicode(s):
    """Make sure a string is unicode, by decoding it used the console LANG,"en_US.utf8" for example"""
    if type(s) == str:
        return s.decode(sys.getfilesystemencoding())
    return s

class NetworkServices:
    """These are simple functions to interact with the network.
       mDNS (Multicast DNS) is a network service that allows hostnames to be resolved without an external DNS server.
       Hostnames are resolved using the ".local" domain.
       Alternatively to using the python Zeroconf package, we
