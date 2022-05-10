import codecs
# Test codecs.register_error('strict', codecs.ignore_errors)

# The following is a test of the codecs module.

# The codecs module defines a set of base classes which define the
# interface and can also be used to easily write your own codecs for
# use in Python.

# Written by Marc-Andre Lemburg (mal@lemburg.com).

# (c) Copyright CNRI, All Rights Reserved. NO WARRANTY.

# *************************************************************

# The following tests exercise the StreamWriter and StreamReader
# classes.

# Note: the test_* functions in this module must *not* raise exceptions
#       since that confuses the test framework.

import unittest
import io
import codecs
import sys
import os
