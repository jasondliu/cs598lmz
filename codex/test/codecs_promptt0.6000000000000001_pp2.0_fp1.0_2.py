import codecs
# Test codecs.register_error before importing other modules
# that might also try to register errors.
try:
    codecs.register_error('test.test_codecs', codecs.lookup_error('strict'))
except ValueError:
    pass
import re
import os
import sys
import unittest
import warnings
