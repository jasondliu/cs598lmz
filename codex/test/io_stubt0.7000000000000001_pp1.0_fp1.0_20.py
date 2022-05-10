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

# This function is currently used to delay exit until the
# background threads finish a test.  It may go away.
def wait_threads(wait=True):
    import threading
    for i in range(1000):
        if not threading.active_count() > 1:
            if wait:
                time.sleep(0.1)
            return
        time.sleep(0.01)
    raise Exception("wait_threads didn't work")


#
# ___________________________________________________________________________
# Support for bigaddrspacetest.py
#

# This class is used in test_large_mappable_as_parameter()
