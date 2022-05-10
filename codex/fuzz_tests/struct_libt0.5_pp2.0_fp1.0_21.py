import _struct
import sys
import time
import traceback

try:
    import cPickle as pickle
except ImportError:
    import pickle

try:
    import numpy
except ImportError:
    numpy = None

# Python 2/3 compatibility
try:
    unicode
except NameError:
    unicode = str

# Python 2/3 compatibility
try:
    long
except NameError:
    long = int

# Python 2/3 compatibility
try:
    basestring
except NameError:
    basestring = str

# Python 2/3 compatibility
try:
    xrange
except NameError:
    xrange = range

# Python 2/3 compatibility
try:
    from cStringIO import StringIO
except ImportError:
    from io import BytesIO as StringIO

# Python 2/3 compatibility
try:
    from itertools import izip
except ImportError:
    izip = zip

# Python 2/3 compatibility
try:
    from itertools import imap
except ImportError:
    imap
