from _struct import Struct
s = Struct.__new__(Struct)
s.__doc__ = b'1sh'
print(s.__doc__)

try:
    import brotli
    from brotli import Compressor, decompress
    from brotli import ENABLE_DICTIONARY, get_dictionary
except ImportError:
    brotli = None

try:
    import zlib
except:
    zlib = None

class Socks5Message:

    # socks request
    SOCKS_VERSION_5 = 5
    SOCKS_METHOD_NO_AUTHENTICATION = 0
    SOCKS_METHOD_LOGIN = 2
    SOCKS_METHOD_USERPASS = 0

    # socks reply
    SOCKS_REPLY_SUCCESS = 0
    SOCKS_REPLY_REFUSED = 5
    SOCKS_REPLY_NETWORK_UNREACHABLE = 3
    SOCKS_REPLY_HOST_UNREACHABLE = 4
    SOCKS_REPLY_CONNECTION_REFUSED = 5
    SOCKS
