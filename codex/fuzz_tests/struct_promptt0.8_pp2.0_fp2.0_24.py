import _struct
# Test _struct.Struct with big endian format.
from _struct import Struct
import _string
# Test string.ascii_letters and string.ascii_lowercase
import string
from string import ascii_letters, ascii_lowercase
# Test tokenize.String.
from tokenize import String
# Test copyreg.constructor and copyreg.add_extension.
from copyreg import constructor, add_extension
import sys
# Test sys.getsizeof, sys.exit and sys.api_version
from sys import getsizeof, exit, api_version
from sys import getsizeof as func_getsizeof
from sys import exit as func_exit
from sys import api_version as var_api_version

class A:
    def __init__(self, a, b):
        pass

class B:
    def __init__(self, b):
        pass

    def __getitem__(self, key):
        return key

def func_0(a, b):
    pass

def func_1(a):
    pass

def func_2(a=
