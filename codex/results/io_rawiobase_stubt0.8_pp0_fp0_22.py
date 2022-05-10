import io
class File(io.RawIOBase):
    def __init__(self,filepath,mode,*args,**kwargs):
        self._filepath = filepath
        self._mode = mode
        self._args = args
        self._kwargs = kwargs
        self._file = None

    def open(self):
        subprocess.call(['open',self._filepath])
    def _open(self):
        self._file = open(self._filepath,self._mode,*self._args,**self._kwargs)
        return self._file
    def close(self):
        self._file.close()
    def fileno(self):
        return self._file.fileno()
    def flush(self):
        self._file.flush()
    def isatty(self):
        return self._file.isatty()
    def readable(self):
        return self._file.readable()
    def readinto(self,buffer):
        return self._file.readinto(buffer)
    def readline(self,limit=-1):
        return self._file.readline(limit)

