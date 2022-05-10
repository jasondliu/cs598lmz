import io
class File(io.RawIOBase):
  def __init__(self, name, mode='r'):
    self._name = name
    self._mode = mode
    self._file = None
    self.open()
  def open(self):
    if self._file is None:
      self._file = open(self._name, self._mode)
      self.seek(0)
    return self._file
  def close(self):
    if self._file:
      self._file.close()
      self._file = None
  def fileno(self):
    f = self.open()
    return f.fileno()
  def readable(self):
    f = self.open()
    return f.readable()
  def readline(self, size=-1):
    f = self.open()
    return f.readline(size)
  def read(self, size=-1):
    f = self.open()
    return f.read(size)
  def seek(self, offset, whence=io.SEEK_SET):
    f = self.open()
    return f.seek(offset
