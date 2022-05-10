import mmap
import os
import sys
import re
import math

def main():
    print('This is main of module "mytools"')
    f = open("/home/martin/testfile", "r")
    s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    #if s.find('\0') != -1:
    #    print('null byte in there')
    #else:
    #    print('no null byte')
    #print(s)
    print(os.getcwd())
    #print(sys.argv[0])
    print(os.path.dirname(sys.argv[0]))
    a = re.match(r'\d+', 'afasdfas234asdfasdf')
    print(a)
    print(math.sqrt(4))

