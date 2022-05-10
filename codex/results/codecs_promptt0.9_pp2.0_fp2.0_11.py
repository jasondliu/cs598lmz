import codecs
# Test codecs.register_error
try:
    codecs.register_error('spam', None)
except RuntimeError, e:
    assert "implementation" in str(e)
    assert str(int).lower() in str(e)

blocksize = 64
blockmask = blocksize -1 

class MmapBytesIO(object):
    def __init__(self, shmname, size, st_mode=0666):
        self.size = size
        self.pos = 0
        self.closed = False
        self.last_page_number = (size >> 13) + 1
        self.fd = ISHM.open(shmname, size = size, st_mode = st_mode)

    def __del__(self):
        self.close()

    def close(self):
        pass;
