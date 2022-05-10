import codecs
# Test codecs.register_error
import errno
# Import StringIO from cStringIO for efficiency
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import functools
import gc
import gettext
import glob
import hashlib
# hatfile should be imported before heapq
try:
    import hatfile
except ImportError:
    pass
import heapq
import imp
import inspect
import itertools
import linecache
import locale
import logging
import math
import mmap
import ntpath
import operator
import optparse
import os
import pdb
import pickle
import platform
import pprint
import profile
import pstats
import random
import re
