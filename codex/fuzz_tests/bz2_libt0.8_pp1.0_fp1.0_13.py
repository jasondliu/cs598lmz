import bz2
bz2.decompress(bz2.compress(msg)) == bz2.compress(msg)

import hashlib
import os
os.getpid()
hashlib.md5(msg).digest_size

import pickle
pickle.dumps(msg)
pickle.loads(pickle.dumps(msg)) == msg

import zlib
zlib.compress(msg)
zlib.decompress(zlib.compress(msg)) == zlib.compress(msg)

import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
   'yellow'], 'blue']]]
pprint.pprint(t, width=30)

import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""
print(textwrap.fill(doc, width=40))

import re
re.findall(r'\bf[a-z]*',
