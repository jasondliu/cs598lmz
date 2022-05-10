import io
class File(io.RawIOBase):
  def __init__(self, name, mode):
    io.RawIOBase.__init__(self)
    self._name = name
    self._mode = mode

  def close(self):
    pass

  def readable(self):
    return True

  def seek(self, offset, whence=0):
    return -1

  def seekable(self):
    return False

  def tell(self):
    return -1

  def writable(self):
    return False

print(File.__bases__)
