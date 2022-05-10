import types
# Test types.FunctionType()
def dummy():
    pass
ret = types.FunctionType(dummy.__code__, {}, dummy.__name__, dummy.__defaults__, dummy.__closure__)
assert ret() is None
# Issue #28552: On Windows, inspect.getmro()'s behavior changed across Python 3.5 and 3.6. See
# <https://bugs.python.org/issue28552>.
# Note: We don't test classes with metaclass because metaclass and abc.ABCMeta is only
# supported on Python 3.6+.
import inspect
def test_getmro(cls, expected_mro):
    assert inspect.getmro(cls) == expected_mro
from collections import OrderedDict
class TestClass:
    def __init__(self):
        a = OrderedDict()
        test_getmro(TestClass, (TestClass, object))
# Test os.write() on integer
# Test os.write() on str
import os
str1 = b'hello world'
str2 = 'hello world'
fd =
