gi = (i for i in ())
# Test gi.gi_code.co_argcount, gi.gi_code.co_flags, gi.gi_code.co_name
#
# This is a much more thorough test than test_generators.py.
#

import sys
import types
import unittest
import pickle
from test import support

# GeneratorExit inherits from BaseException, not Exception.
# This is intentional, since it is not meant to be caught by
# a "except Exception:" clause.
#
# Note: The following is true for CPython only.
#
# This is a consequence of PEP 479, which changed the semantics of
# StopIteration.  In Python 2, "except Exception:" catches both
# StopIteration and GeneratorExit.  In Python 3, it only catches
# StopIteration, which is a subclass of Exception, but not GeneratorExit.
#
# GeneratorExit is meant to be caught by a "except StopIteration:" clause,
# which is the normal way to catch exceptions raised by yield from.
#
# This implementation of GeneratorExit is necessary for
# PEP 380's "yield from" syntax to work
