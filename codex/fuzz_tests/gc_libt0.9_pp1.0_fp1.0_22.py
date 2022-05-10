import gc, weakref
import sys, os, re
import time, datetime, calendar
import binascii
from random import random
from collections import OrderedDict, namedtuple
from itertools import islice
from io import BytesIO, StringIO, BufferedWriter
from io import IOBase  # pytype: disable=pyi-error
from functools import partial, update_wrapper

from pywbem.utils import is_text_type

if pywbem.PY2:
    # Python 2
    import cPickle as pickle
else:
    # Python 3
    import pickle  # noqa: F401    # pylint: disable=unused-import

#==============================================================================
# The query/caching module, but without the caching capability, and without
# the inter dependencies on the server side WBEMConnection.
# wbem.query contains all the query parsing and evaluation, handled using
# pull-parsing, which is more efficient than push-parsing, when handling large
# amounts of objects.
#==============================================================================
import pywbem
from py
