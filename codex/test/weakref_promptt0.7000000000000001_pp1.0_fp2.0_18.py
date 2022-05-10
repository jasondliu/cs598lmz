import weakref
# Test weakref.ref() and weakref.proxy() for strs
import gc
import operator
import pickle
import struct
import sys
import unittest
from test.support import run_unittest, TESTFN, check_py3k_warnings, is_jython
import test.support as support


