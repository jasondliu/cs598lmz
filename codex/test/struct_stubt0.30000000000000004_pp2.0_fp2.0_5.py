from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<3s3sHH'
s.size = calcsize(s.format)

def unpack_from(buffer, offset=0):
    return s.unpack_from(buffer, offset)

def pack_into(buffer, offset, host, port, hlen, plen):
    return s.pack_into(buffer, offset, host, port, hlen, plen)

def calcsize():
    return s.size

#
# Exceptions
#

class Socks5Error(Exception):
    pass

class Socks5AuthError(Socks5Error):
    pass

class Socks5ServerError(Socks5Error):
    pass

class Socks5NetworkError(Socks5Error):
    pass

class Socks5GeneralError(Socks5Error):
    pass

class Socks5CommandError(Socks5Error):
    pass

class Socks5AddressError(Socks5Error):
    pass

#
# Constants
#

SOCKS5_VERSION = 5

