import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f # break reference cycle

try:
    import faulthandler
    import gc
    faulthandler.enable()

    # Ensure that garbage collection of the faulthandler
    # global_fds is delayed until the (C) io buffer is released.
    faulthandler.dump_traceback_later(7, repeat=True)
    del view
    gc.collect()
    time.sleep(2)
except ImportError:
    pass
