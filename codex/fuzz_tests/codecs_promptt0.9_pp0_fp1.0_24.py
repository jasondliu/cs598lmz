import codecs
# Test codecs.register_error
## unicode with specific encoding
# self.encoding = code
import binascii
binascii.a2b_uu('\u0100\u0000\u0500\u0001')

prog = re.compile('^\s*$')
prog2 = re.compile('^x*$')

import cmd
import unittest
import time

icmp = socket.getprotobyname('icmp')

import pwd

# test error callback from C which includes an exception class
import base64

def _test_function(x):
    "This is docstring."
    global _test_function_var
    _test_function_var = x
    return x

def _test_function2():
    global _test_function_var
    _test_function_var = _test_function_var + 3
    return False

class test_class:
    def __init__(self, x):
        self.x = x
    def _test_method(self, x):
        return x * self.x
   
