import mmap
import os
import re
import sys

curr = os.getcwd()
#print curr

NAME = "esp"

def hex2dec(s):
    return int(s, 16)

def dec2hex(s):
    return hex(s)

def checksum(s):
    #s = "".join(s.split())
    #print "s:",s
    b = bytearray.fromhex(s)
    return (~sum(b)) & 0xFF

def parse(s):
    #print s
    s = re.sub('[^0-9a-fA-F]','', s)
    #print s
