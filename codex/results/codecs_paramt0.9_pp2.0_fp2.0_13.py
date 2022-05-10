import codecs
codecs.register_error("strict", codecs.ignore_errors)
import collections; from collections import Counter

from six import iteritems
from six import iterkeys
from six import itervalues
from six.moves import range

import os
import math
import sys
import errno
from six import string_types
from six import text_type
from six import binary_type
from six.moves import xrange
from six.moves import xmlrpc_client

# OrderedDict is new in 2.7
try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

from tensorflow.python.platform import gfile
import numpy as np

PY3 = sys.version_info[0] == 3


# Text file I/O

class SmartOpen(object):
    """Opens a file intelligently, transparently using gzip and bz2 if needed.
    
    The file can be read or written depending on the mode.
    If a file to be written ends in .gz or .bz2, it will be compressed accordingly
