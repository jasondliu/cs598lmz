from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type([]))
print(type(1))
print(type(int))
print(type(str))
print(type(None))
print(type(FunctionType))
print(type(lambda x: x))

import sys
print(sys.argv)

import os
print(os.path.abspath('.'))

import random
print(random.choice([1, 2, 3]))

from io import StringIO, BytesIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())

f = StringIO('hello\nworld\n')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

from PIL import Image
im = Image.open('../../resource/image/test.jpg
