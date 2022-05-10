import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
conn = sqlite3.connect('d:/tmp/test.db')
print conn

# Test ctypes.util.find_library()
print ctypes.util.find_library('c')

# Test threading.get_ident()
print threading.get_ident()
</code>
All of above works well on my local machine(Windows 7) and on the VPS(server) which is also Windows 7. 
But when I upload my code to Amazon EC2(Ubuntu 12.04), there are errors.
<code>Traceback (most recent call last):
  File "/home/ubuntu/myapp/myapp/views.py", line 8, in &lt;module&gt;
    import sqlite3
  File "/usr/lib/python2.7/sqlite3/__init__.py", line 24, in &lt;module&gt;
    from dbapi2 import *
  File "/usr/lib/python2.7/sqlite3/dbapi2.py", line 27, in &lt;module&gt;
    from _sqlite3 import *
