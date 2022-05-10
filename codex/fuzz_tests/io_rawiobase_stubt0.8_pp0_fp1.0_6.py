import io
class File(io.RawIOBase):
 def __init__(self, name: str, mode: str = 'U', *args, **kwargs):
  self.file = io.open(name, mode, *args, **kwargs)
  self.encoding = self.file.encoding
 def __enter__(self):
  self.file.__enter__()
  return self
 def __exit__(self, *args, **kwargs):
  self.file.__exit__(*args, **kwargs)
 def flush(self):
  self.file.flush()
 def fileno(self):
  return self.file.fileno()
 def isatty(self):
  return self.file.isatty()
 def read(self, n = -1):
  return self.file.read(n)
 def readable(self):
  return True
 def readline(self, limit=-1):
  return self.file.readline(limit)
 def readlines(self, hint=-1):
  return self.file.readlines(hint)
 def seek(self, offset, whence=io.SEEK
