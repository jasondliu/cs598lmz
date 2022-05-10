import _struct
# Test _struct.Struct
from test.libregrtest.refleak import structseq
from test.support.script_helper import assert_python_ok
from test.support.script_helper import spawn_python
from test.support import findfile
from test.support import forget
from test.support import import_helper
from test.support import run_unittest
from weakref import proxy


class BadCmp:
    def __eq__(self, other):
        raise Exc()

    def __ne__(self, other):
        raise Exc()


class Exc(Exception):
    pass


class X:
    def __init__(self, a):
        self.a = a

    def set(self, a):
        self.a = a

    def __hash__(self):
        return hash(self.a)


class Y(X):
    def __lt__(self, other):
        # Implementing __lt__ makes the class sortable
        return self.a < other.a


class Z(X):
    def __eq__(self, other):
        return self
