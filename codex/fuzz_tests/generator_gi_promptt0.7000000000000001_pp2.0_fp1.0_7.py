gi = (i for i in ())
# Test gi.gi_code
# gi.gi_code.co_name
# Test gi.gi_frame
def f():
    yield 1
    yield 2
gi = f()
# gi.gi_frame.f_locals
# Test gi.gi_frame.f_trace
def g():
    return
gi = g()
# Test gi.gi_running
# Test gi.gi_yieldfrom
# Test hasattr
# hasattr(None, 'abc')
# Test hash
# hash(None)
# Test hex
# hex(0)
# Test id
# id(0)
# Test input
# input()
# Test int
# int()
# int(0)
# int(0.0)
# Test isinstance
# isinstance(0, int)
# Test issubclass
# issubclass(int, int)
# Test iter
# iter(dict())
# Test len
# len(dict())
# Test list
# list()
# Test locals
# locals()
# Test map
# list(map(int, ['1', '2']
