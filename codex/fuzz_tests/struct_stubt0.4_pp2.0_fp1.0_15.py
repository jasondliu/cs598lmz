from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('hhl')
print(s.size)
print(s.pack(1, 2, 3))
print(s.unpack(b'\x00\x01\x00\x02\x00\x00\x00\x03'))

import os
print(os.path.basename('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.join('tmp', 'test.txt'))
print(os.path.expanduser('~'))
print(os.path.splitext('/tmp/test.txt'))

import glob
print(glob.glob('*.py'))

import sys
print(sys.argv)

import re
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))

import math

