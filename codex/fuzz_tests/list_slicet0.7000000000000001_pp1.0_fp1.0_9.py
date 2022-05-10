import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])

try:
    from xml.etree.cElementTree import Element, SubElement, fromstring, tostring
except ImportError:
    from xml.etree.ElementTree import Element, SubElement, fromstring, tostring

import gzip
import os
import re
import struct
import sys
import tempfile
import time

try:
    import zlib
except ImportError:
    zlib = None

try:
    import bz2
except ImportError:
    bz2 = None

try:
    import lzma
except ImportError:
    lzma = None

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

try:
    import hashlib
except ImportError:
    import md5
    import sha
    class hashlib(object):
        md5 = md5.new
        sha1 = sha.new

try:
    from sys import maxsize
except ImportError:
    from sys import maxint as maxsize

try:
    from sys
