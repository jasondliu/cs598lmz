import io
class File(io.RawIOBase):
    def __init__(self):
        pass

    def write(self, b):
        return True

    def readable(self):
        return True

    def readinto(self, b):
        b[:] = [0x80] * len(b)
        return len(b)

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        return 0

    def tell(self):
        return 0

    def close(self):
        pass

sys.modules['machine'] = machine
sys.modules['pyb'] = pyb
sys.modules['uio'] = uio
sys.modules['uerrno'] = uerrno
sys.modules['uselect'] = uselect
sys.modules['utime'] = utime
sys.modules['uos'] = uos
sys.modules['pin'] = pin
sys.modules['gc'] = gc
sys.modules['os'] = os
sys.modules['uco
