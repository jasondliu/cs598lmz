gi = (i for i in ())
# Test gi.gi_code == types.FunctionType
# Test gi.gi_frame

def f():
    for i in (1,2,3):
        yield i
a = f()
# Test a.gi_code = f.func_code
# Test a.gi_frame = f.func_code

# Test that methods are methods, not functions
# (methods have im_func, not func_code, etc)
class A:
    def foo(self):
        pass
a = A()
a.foo.func_code
#TestError[TypeError]
a.foo.func_defaults
#TestError[TypeError]
a.foo.func_doc
#TestError[TypeError]
a.foo.func_globals
#TestError[TypeError]
a.foo.func_name
#TestError[TypeError]

# Test support for nested scopes

def f():
    x = 3
    def g():
        print x
    g()
f()

def f():
    x = 3
    def g():
        print x
    return
