import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is a workaround for a bug in the Python interpreter:
#  http://bugs.python.org/issue1602
# The Python interpreter pre-compiles bytecode as a speed optimization.
# If Python crashes in the middle of this process, the bytecode can
# become corrupted.  The linecache module attempts to parse the
# bytecode to get information about the source code that needs to be
# printed.  This can crash Python again.  The bug is particularly
# common on Windows, because Windows users are likely to have modified
# their PATH to include directories with non-ASCII characters.  Such
# directories cannot be added to sys.path using the traditional
# mechanism, because sys.path is stored as a str, and on Windows, str
# does not support non-ASCII characters.  The work-around is to switch
# sys.path to use Unicode.
if sys.platform == 'win32':
    sys.path = [path.decode(sys.getfilesystemencoding()) for path in sys.path]

# Set up a handler for the interrupt signal.
