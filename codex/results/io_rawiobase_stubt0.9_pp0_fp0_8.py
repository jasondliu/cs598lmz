import io
class File(io.RawIOBase):
    def __init__(self,name,mode="r",hold=2147483648,pack=800,bufsize=4096,encoding=None):
        # hold is optional maximum number of bytes to keep in memory
        # pack is optional size to flush
        # ignore encoding for now
        assert bufsize>0,"must have bufsize larger than 0"
        assert pack>=0,"must have pack come in to play immediately"
        assert hold>0,"must have hold larger than 0"
        self._fname = name
        self._mode = mode
        self._bufsize = bufsize
        # temp buffer
        self._tbuf = bytearray()
        # buffer
        self._buf = bytearray()
        self.tell_chk()
        self.read_chk()
        self.write_chk()
        self.seekable_chk()
        if 'a' in self._mode:
            self._dell = len(self._buf)
        else:
            self._dell = 0
        # handle failed seek
        self._p0
