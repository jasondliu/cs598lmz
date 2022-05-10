import mmap
import subprocess
import xml.etree.ElementTree as ET
import sys

def cmp(s1, s2):
    if s1 == s2:
        return 0
    elif s1 < s2:
        return -1
    else:
        return 1

def get_next_value(val):
    if val.isdigit():
        return str(int(val) + 1)
    else:
        if ord(val) == ord('z'):
            return 'a'
        elif ord(val) == ord('Z'):
            return 'A'
        else:
            return str(unichr(ord(val)+1))

def incr(s):
    if len(s) == 0:
        return 'a'
    else: 
        if cmp(get_next_value(s[-1]), 'A') == 0:
            return s[0:-1] + 'A'
        elif cmp(get_next_value(s[-1]), 'z') == 0:
            return s[0
