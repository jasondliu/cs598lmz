import _struct
# Test _struct.StructBuild and _struct.StructParse
#
# This test script tests:
# - _struct.StructBuild
# - _struct.StructParse
#
# When StructBuild is passed an exception is thrown, if:
# - StructFormat is not a string.
# - The format of StructFormat is invalid.
# - Actual arguments differ.
#
# When StructParse is passed an exception is thrown, if:
# - The string size is invalid.
# - StructFormat is not a string.
# - The format of StructFormat is invalid.
#
# When StructBuild and StructParse is passed an exception is thrown if:
# - Expected and actual arguments differ.

import exceptions
import re
import string
import sys
import unittest

import _struct  # C implementation of ``struct`` module

# regular expressions describing format of struct format strings
