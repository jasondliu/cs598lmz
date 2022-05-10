import _struct
# Test _struct.Struct
_struct.Struct('i')

# Test array.array
import array
array.array('i')

# Test hashlib
import hashlib
hashlib.md5()

# Test itertools
import itertools
itertools.count()

# Test mmap
import mmap
mmap.mmap()

# Test re
import re
pat = re.compile('hello')
pat.match('world')

# Test socket
import socket
sock = socket.socket()

# Test ssl
import ssl
ssl.SSLSocket()

# Test struct
import struct
struct.pack('i', 5)

# Test zlib
import zlib
compressobj = zlib.compressobj()
compressobj.compress(b'hello')

# Test sys
import sys
sys.displayhook(5)

# Test time
import time
time.monotonic()

# Test math
import math
math.log(5)

# Test _elementtree
from xml.etree import _elementtree
_elementtree.parse
