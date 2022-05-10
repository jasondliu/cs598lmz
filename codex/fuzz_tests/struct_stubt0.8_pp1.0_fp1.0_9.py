from _struct import Struct
s = Struct.__new__(Struct)
s

import sys
from _io import FileIO
f = FileIO.__new__(FileIO, 'example.txt')
f

from time import time as my_time
my_time()

from collections import OrderedDict
d = OrderedDict.__new__(OrderedDict)
d

from fractions import Fraction
f = Fraction.__new__(Fraction, 2, 3)
f

from array import array
a = array.__new__(array, 'I', [1, 2, 3])
a

from urllib.request import urlopen
from contextlib import closing
with closing.__new__(closing, urlopen('http://www.python.org')) as page:
    for line in page:
        print(line)

import shelve
db = shelve.open('test.db')
db = shelve.__new__(shelve, 'test.db')
db

from dbm import ndbm
db = ndbm.__new__(ndbm, 'example.db')
db
