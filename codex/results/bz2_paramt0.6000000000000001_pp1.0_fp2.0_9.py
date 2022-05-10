from bz2 import BZ2Decompressor
BZ2Decompressor()

# Test for bz2.compress
from bz2 import BZ2Compressor
BZ2Compressor()

# Test for ftplib.FTP_TLS
try:
    from ftplib import FTP_TLS
    FTP_TLS
except:
    pass

# Test for hashlib.pbkdf2_hmac
try:
    from hashlib import pbkdf2_hmac
    pbkdf2_hmac
except:
    pass

# Test for http.client.HTTPSConnection
try:
    from http.client import HTTPSConnection
    HTTPSConnection
except:
    pass

# Test for http.client.HTTPSConnection
try:
    from http.client import HTTPSConnection
    HTTPSConnection
except:
    pass

# Test for http.client.HTTPSHandler
try:
    from http.client import HTTPSHandler
    HTTPSHandler
except:
    pass

# Test for http.server.HTTPServer
try:
    from http.server import HTTPServer
    HTTPServer
except:
    pass


