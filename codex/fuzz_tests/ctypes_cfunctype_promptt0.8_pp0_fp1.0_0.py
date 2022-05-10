import ctypes
# Test ctypes.CFUNCTYPE
#
contextlib.contextmanager
def dummy_context_manager():
    yield

dummy_pointer = ctypes.POINTER(ctypes.c_int)
dummy_proc_fn = ctypes.CFUNCTYPE(ctypes.c_void_p, dummy_pointer)

dummy_proc_fn(dummy_context_manager())

# Test 'with' statement
with dummy_context_manager():
    x = 'foo'
    print(x)

# Test 'with' statement with multiple managers
with dummy_context_manager(), dummy_context_manager():
    x = 'foo'
    print(x)

contextlib.suppress

# Test 'with' statement that re-raises an exception
def dummy_gen():
    yield 1
    raise RuntimeError()

g = dummy_gen()

with contextlib.suppress(RuntimeError):
    next(g)

try:
    next(g)
except RuntimeError:
    pass

# Test contextlib.redirect_stdout() with a file
import io
import
