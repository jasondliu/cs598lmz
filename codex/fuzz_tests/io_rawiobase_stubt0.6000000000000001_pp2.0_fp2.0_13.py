import io
class File(io.RawIOBase):
  def __init__(self, file_path, mode="r"):
    self._file = open(file_path, mode)
  def read(self, length=None):
    return self._file.read(length)
  def close(self):
    self._file.close()
  def readable(self):
    return True
  def writable(self):
    return False
  def seekable(self):
    return False
  def seek(self, offset, whence):
    raise io.UnsupportedOperation
  def tell(self):
    raise io.UnsupportedOperation
  def flush(self):
    raise io.UnsupportedOperation
  def write(self, data):
    raise io.UnsupportedOperation
  def writelines(self, lines):
    raise io.UnsupportedOperation
  def __enter__(self):
    return self
  def __exit__(self, type, value, traceback):
    self.close()
    return False

class FileSink(io.RawIOBase):
  def __init__(self, file_path, mode="w
