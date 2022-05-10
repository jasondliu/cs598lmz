import io
class File(io.RawIOBase):
  def __init__(self, filename, mode='r'):
    self.name = filename
    if mode not in ['r', 'w']:
      raise NotImplemented
    self.mode = mode
    self.file = open(filename, mode)

  def write(self, string):
    if self.mode != 'w':
      raise IOError
    self.file.write(string)

  def fileno(self):
    return self.file.fileno()

  def close(self):
    self.file.close()

  def readable(self):
    return self.mode == 'r'

  def writable(self):
    return self.mode == 'w'

  def seekable(self):
    return self.file.seekable()

  def seek(self, offset, whence=0):
    return self.file.seek(offset, whence)

  def tell(self):
    return self.file.tell()

  def read(self, size=-1):
    return self.file.read(size)

  def readinto(self, b):
