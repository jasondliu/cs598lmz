import ctypes
# Test ctypes.CFUNCTYPE.

import ctypes
import unittest
from test import support

# A simple C function
SDL_Init = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_uint)(("SDL_Init", ctypes.cdll.LoadLibrary(None)))

class SimpleFunctionTestCase(unittest.TestCase):
    def testSimpleFunction(self):
        "Tests a CFUNCTYPE function with no arguments"
        # http://pygame.org/wiki/SDL_Init?parent=CookBook
        self.assertEqual(SDL_Init(0), 0)

# This function parses 'char ** argv' and returns the argv words
# as a list of python strings.
Parse = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(ctypes.POINTER(ctypes.c_char)))(("parse", ctypes.cdll.LoadLibrary(None)))

class ArgvFunctionTestCase(unittest.TestCase):

    def test_parse_arg
