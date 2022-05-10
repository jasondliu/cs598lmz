import types
# Test types.FunctionType

from java.lang import System
from org.python.core.util import StringUtil

if 1:
    def add(x, y):
        return x + y

    class Test:

        def __init__(self, n):
            self.n = n

        def add(self, x, y):
            return x + y + self.n

    if types.FunctionType is not None:
        a = add
        if not isinstance(a, types.FunctionType):
            raise AssertionError

        a = Test(4).add
        if not isinstance(a, types.FunctionType):
            raise AssertionError


# Test types.CodeType

from java.lang import System
from org.python.core.util import StringUtil

if 1:
    def add(x, y):
        return x + y

    class Test:

        def __init__(self, n):
            self.n = n

        def add(self, x, y):
            return x + y + self.n

    if types.CodeType is not None
