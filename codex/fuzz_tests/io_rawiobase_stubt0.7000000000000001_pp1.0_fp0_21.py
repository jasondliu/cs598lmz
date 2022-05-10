import io
class File(io.RawIOBase):
    def __init__(self):
        pass
    def seek(self, offset, whence=0):
        pass
    def tell(self):
        return 0
    def writable(self):
        return True
    def readable(self):
        return True
    def seekable(self):
        return True
    def flush(self):
        pass
    def readinto(self, b):
        return 0
    def write(self, b):
        return 0
    def close(self):
        pass
    def fileno(self):
        return 0

#==============================================================================
# thread
#==============================================================================
import threading
def start_new_thread(function, args, kwargs={}):
    t = threading.Thread(target=function, args=args, kwargs=kwargs)
    t.start()
    return t

class Lock(object):
    def __init__(self):
        self._lock = threading.Lock()
    def acquire(self, *args):
        return self._lock.acquire(*args)
    def release
