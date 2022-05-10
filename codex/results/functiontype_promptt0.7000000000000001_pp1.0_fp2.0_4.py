import types
# Test types.FunctionType
def foo(self):
    return self

assert isinstance(foo, types.FunctionType)
assert foo.__name__ == 'foo'
assert foo.__doc__ is None
# Test types.GeneratorType
def bar():
    yield 1

assert isinstance(bar(), types.GeneratorType)
# Test types.MethodType
class Foo(object):
    pass

bar = foo.__get__(Foo(), Foo)
assert isinstance(bar, types.MethodType)
assert bar.__self__.__class__ == Foo
assert bar.__func__ == foo
# Test types.ModuleType
import sys
assert isinstance(sys, types.ModuleType)
assert sys.__name__ == 'sys'
assert sys.__doc__.startswith('This module provides access')
# Test types.TracebackType
try:
    raise ValueError()
except ValueError:
    import sys
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)
    assert tb.tb_frame
