import types
types.MethodType(foo, None, Bar)

# Bug: http://bugs.python.org/issue11645
import types
class Bar(object):
    pass
types.MethodType(lambda: 0, None, Bar)

import types
def foo():
    pass
types.MethodType(foo, None, type)

import types
def foo():
    pass
types.MethodType(foo, None, type)

import types
def foo():
    pass
types.MethodType(foo, None, int)

import types
def foo():
    pass
types.MethodType(foo, None, int)

class Bar(object):
    pass
def foo():
    pass
types.MethodType(foo, None, Bar)

import types
class Bar(object):
    pass
def foo():
    pass
types.MethodType(foo, None, Bar)

# Bug: http://bugs.python.org/issue11645
import types
class Bar(object):
    pass
types.MethodType(lambda: 0, None, Bar)

# Bug: http://bugs.
