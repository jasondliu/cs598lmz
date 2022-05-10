gi = (i for i in ())
# Test gi.gi_code.co_filename

# Test that code objects are not reused
import sys
def f():
    sys.stdout.write("hello")
g = f.__code__
f()
g = f.__code__
f()
g = f.__code__
f()

# Test that we don't segfault when printing a traceback from an exception
# that was created using PyErr_SetString
try:
    raise ValueError("hello")
except ValueError:
    import traceback
    traceback.print_exc()

# Test that we can't create a code object with a non-str filename
# and non-str name
try:
    compile(b"x", b"x", "exec")
except TypeError:
    print("TypeError")

# Test that we can't create a code object with a non-str filename
# and a non-str name
try:
    compile(b"x", "<x>", "exec")
except TypeError:
    print("TypeError")

# Test that we can't create a code object with a non-str
