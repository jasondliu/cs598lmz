fn = lambda: None
# Test fn.__code__ and fn.func_code
# This test should pass, and should not crash.
sys.settrace(fn)
sys.settrace(fn)

def f():
    pass
# Test f.__code__ and f.func_code
# This test should pass, and should not crash.
sys.settrace(f)
sys.settrace(f)

class Foo(object):
    def method(self):
        pass
# Test Foo.method.__code__ and Foo.method.func_code
# This test should pass, and should not crash.
sys.settrace(Foo.method)
sys.settrace(Foo.method)

# Test sys.settrace with a function which returns None.
def test_settrace_None(self):
    def foo(frame, event, arg):
        return None
    def bar():
        pass
    sys.settrace(foo)
    sys.settrace(None)
    bar()
    sys.settrace(foo)
    sys.settrace(None)
    bar()
    sys.settrace(foo)
