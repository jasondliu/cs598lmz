fn = lambda: None
# Test fn.__code__.co_name
assert(fn.__code__)

# Test fn.__code__.co_firstlineno
fn = lambda: None
assert(fn.__code__.co_firstlineno)

# Test python compiled code comment
# fn.__code__.co_file
fn = lambda: None
assert(fn.__code__.co_filename)

# fn.__code__.co_flags
fn = lambda: None
assert(fn.__code__.co_flags)

s = "print('hello world')"
# Test compile()
code = compile('print("hello world")', '', 'exec')
assert(code)

# Test sys.getsizeof()
import sys
import _threading_local
assert(sys.getsizeof(_threading_local.local())>=32)
assert(sys.getsizeof(_threading_local.local(a='a', b=1, c=None))>=32)

# Test lambda
fn = lambda a: a if a is not None else 0
assert(fn(1) == 1
