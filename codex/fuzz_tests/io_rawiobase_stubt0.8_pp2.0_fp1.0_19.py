import io
class File(io.RawIOBase):
  def __init__(self, file_name, mode):
    self.obj = open(file_name, mode)
  def readable(self):
    return super().readable()
  def writable(self):
    return super().writable()
  def readinto(self, b):
    return super().readinto(b)
  def write(self, b):
    return super().write(b)
  def seekable(self):
    return super().seekable()
  def seek(self, offset, whence=0):
    return super().seek(offset, whence)
  def tell(self):
    return super().tell()
  def __enter__(self):
    return self
  def __exit__(self, ext, exa, tb):
    return self.obj.__exit__(ext, exa, tb)
  def close(self):
    return self.obj.close()

class SameRow(tuple):
  def __new__(cls, *args):
    return tuple.__new__(cls, args)

class Mini
