gi = (i for i in ())
# Test gi.gi_code.co_name

def foo():
    yield 2
    yield 2
    yield 2

def bar():
    for i in foo():
        yield i
    yield 2
    return

def test():
    for i in bar():
        yield i
    return

t = test()
assert t.gi_code.co_name == 'foo'
t.next()
assert t.gi_code.co_name == 'bar'
t.next()
assert t.gi_code.co_name == 'bar'
t.next()
assert t.gi_code.co_name == 'test'
t.next()
assert t.gi_code.co_name == 'test'

# Test gi_frame

def foo():
    return (i for i in ())

assert foo().gi_frame is foo.func_code.co_firstlineno

# Test gi_frame on an exception

try:
    raise StopIteration
except StopIteration:
    t = sys.exc_traceback.tb_frame.f_back.f_
