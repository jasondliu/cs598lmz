import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
#sqlite3.connect(':memory:')
#sqlite3.connect('test.db')

# Test ctypes.util.find_library()
lib = ctypes.util.find_library('sqlite3')
assert lib

# Test ctypes.cdll.LoadLibrary()
test = ctypes.cdll.LoadLibrary(lib)

# Test sqlite3.connect(':memory:') + threading
assert sqlite3.connect(':memory:')
assert threading.current_thread()

# Test sqlite3.connect('test.db')
assert sqlite3.connect('test.db')
</code>
The error is:
<code>Traceback (most recent call last):
  File "C:\PythonTest\Sqlite3Test.py", line 13, in &lt;module&gt;
    assert lib
AssertionError
</code>
I have already added sqlite3.dll to the folder. And I have copied the path to the system environment variables in the control panel. Still, I cannot get it to work.
I am running on
