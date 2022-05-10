import weakref
# Test weakref.ref() and weakref.proxy()
#
# This tests weakref.ref() and weakref.proxy() with a number of different
# types of objects.  It also tests the callback feature of weakref.ref().
#
# Written by: Fred L. Drake, Jr.
#
# Based on test_weakref.py by Guido van Rossum.
#
# Modified to test weakref.proxy() by Anthony Baxter.

import unittest
from test import support
import sys

# Some objects to be used for various tests

class C:
    pass

class D(C):
    pass

class E:
    pass

class F(E):
    pass

class G:
    pass

class H(G):
    pass

class I(H):
    pass

class J:
    def __init__(self, arg):
        self.arg = arg

class K(J):
    pass

class L(J):
    pass

class M(J):
    pass

class N:
    def __init__(self, arg):
