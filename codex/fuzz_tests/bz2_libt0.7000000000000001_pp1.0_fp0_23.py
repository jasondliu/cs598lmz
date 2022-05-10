import bz2
bz2.test_bz2file()

import cPickle
cPickle.test()

import cStringIO
cStringIO.test()

import datetime
datetime.test()

import doctest
doctest.testmod()

import email
email.test()

import ftplib
ftplib.test()

import gzip
gzip.test()

import keyword
keyword.kwlist

import logging
logging.basicConfig(filename="logging.out")
logging.debug("This is a debug message")
logging.error("This is an error message")

import linecache
linecache.checkcache()

import math
math.test()

import opcode
opcode.opmap['STOP_CODE']

import operator
operator.__dict__

import os
os.__dict__

import pdb
pdb.set_trace()

import pickle
pickle.Pickler(file("pickle.out", "w"))

import pprint

import pydoc
pydoc.help("
