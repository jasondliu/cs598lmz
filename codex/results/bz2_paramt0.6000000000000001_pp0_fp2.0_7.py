from bz2 import BZ2Decompressor
BZ2Decompressor()
from base64 import b64encode
b64encode(b'binary\x00string')
from hashlib import md5
md5(b'how to use md5 in python hashlib?').hexdigest()
from struct import pack
pack('>I', 10240099)
from zlib import decompress
decompress(b'x\x9c\xcbH\xcd\xc9\xc9\x07\x00\x06,\x02\x15')
from itertools import groupby
for key, group in groupby('AAABBBCCCAAA'):
    print(key, list(group))
from fractions import Fraction
Fraction(1, 3)
from math import pi
pi
from random import random
random()
from urllib.request import urlopen
for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    line = line.decode('utf-8')
    if 'EST' in line or 'EDT' in line:
        print(line)
from dat
