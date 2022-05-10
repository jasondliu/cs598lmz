import bz2
bz2.compress("hello world")

import zlib
zlib.compress("hello world")

import gzip
gzip.compress("hello world")

import gzip
f = gzip.open("test.gz", "wb")
f.write("hello world")
f.close()

import gzip
f = gzip.open("test.gz", "rb")
print f.read()
f.close()

import cPickle as pickle
pickle.dumps("hello world")

import cPickle as pickle
pickle.dump("hello world", open("test.p", "wb"))

import cPickle as pickle
pickle.load(open("test.p", "rb"))

try:
    raise Exception("hello", "world")
except Exception, e:
    print e.args

try:
    raise Exception("hello", "world")
except Exception, e:
    print e

import sys
print sys.path

import sys
print sys.argv

import sys
print sys.stdout

import sys

