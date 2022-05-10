import codecs
# Test codecs.register_error('strict', strict_errors)
import decimal
import doctest
import itertools
import math
import os
import pickle
import random
import re
import sys
import tempfile
import unittest
import warnings
from test import support
from test.support import TESTFN, unlink, import_module, run_unittest, import_fresh_module, run_with_locale, check_impl_detail
import test.support as support
__all__ = ['TestRound', 'TestFloat', 'TestComplex', 'TestUnicode', 'TestStr',
    'TestByteArray', 'TestTuple', 'TestList', 'TestSet', 'TestFrozenSet',
    'TestDict', 'TestBool', 'TestInt', 'TestLong', 'TestSlice', 'TestEllipsis',
    'TestXRange', 'TestNotImplemented', 'TestClass', 'TestStaticMethod',
    'TestClassAttributes', 'TestSlots', 'TestDescriptors',
    'TestPartial', 'TestSuper', 'TestComplex', 'TestProperties',
    'TestDec
