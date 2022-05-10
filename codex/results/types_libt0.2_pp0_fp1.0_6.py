import types
types.MethodType(lambda self: self.x, None, A)

# Issue #17078: MethodType should not accept a builtin class
import unittest
try:
    types.MethodType(lambda self: self, unittest.TestCase, unittest.TestCase)
except TypeError:
    pass
else:
    print("expected TypeError")

# Issue #17078: MethodType should not accept a builtin class
try:
    types.MethodType(lambda self: self, unittest.TestCase, unittest.TestCase)
except TypeError:
    pass
else:
    print("expected TypeError")

# Issue #17078: MethodType should not accept a builtin class
try:
    types.MethodType(lambda self: self, unittest.TestCase, unittest.TestCase)
except TypeError:
    pass
else:
    print("expected TypeError")

# Issue #17078: MethodType should not accept a builtin class
try:
    types.MethodType(lambda self: self, unittest.Test
