import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

# Issue #26897: segfault when a file is closed while it is garbage-collected
import _io
import weakref
_io._IOBase_finalize(weakref.ref(open("/dev/null")))

# Issue #27496: segfault when a file is closed while it is finalized
import _testcapi
_testcapi._test_finalizing_file()

# Issue #27706: segfault when a file is closed while it is garbage-collected
# in a different thread
import threading
import time
import _io
import weakref

def target():
    time.sleep(0.1)
    _io._IOBase_finalize(weakref.ref(open("/dev/null")))

t = threading.Thread(target=target)
t.start()

# Issue #27788: segfault when a file is closed while it is garbage-collected
# in a child thread
import threading
import time
import _io
import weakref

def target():
    time.sleep(0
