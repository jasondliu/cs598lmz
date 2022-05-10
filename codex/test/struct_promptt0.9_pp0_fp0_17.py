import _struct
# Test _struct.Struct.{pack,unpack}
# (Don't use from _struct import *; bad things can happen, like infinite
# recursion.)
from _struct import Struct, error
import unittest
from test import support
import sys
import ctypes
import itertools

