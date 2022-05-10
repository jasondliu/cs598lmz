fn = lambda: None
# Test fn.__code__.co_filename:


class Foo(object):
    def __call__(self):
        pass
fn = Foo()
fcode = fn.__call__.__code__

print fcode.co_filename
print stubfn.__code__.co_filename

isinstance(stubfn, types.FunctionType)

isinstance(fn, types.FunctionType)

stubfn.__name__
stubfn.__module__
stubfn.__file__
stubfn.__class__

stubfn.__code__
stubfn.__code__.co_argcount
stubfn.__code__.co_nlocals
stubfn.__code__.co_varnames
stubfn.__code__.co_filename
fcode.co_firstlineno
fcode.co_consts
fcode.co_names
fcode.co_filename
fcode.co_code
len(fcode.co_code)

types.MethodType(code.co_code, fn, fn.__class__)


