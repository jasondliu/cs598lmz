import bz2
bz2.compress('asdf')

import gzip
gzip.compress('asdf')

import cPickle
cPickle.loads(cPickle.dumps('asdf'))

import cStringIO
cStringIO.StringIO()

import marshal
marshal.loads(marshal.dumps('asdf'))

import pprint
pprint.pformat('asdf')

import struct
struct.pack('i', 0)

import array
array.array('i', [0])

import itertools
list(itertools.imap(str, [0]))

import random
random.random()

import math
math.sin(0)

import operator
operator.mul(0, 0)

import datetime
datetime.datetime.now()

import collections
collections.deque([0])
