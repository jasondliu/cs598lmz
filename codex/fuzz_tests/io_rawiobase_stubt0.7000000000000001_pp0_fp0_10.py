import io
class File(io.RawIOBase):
  def __init__(self, file_or_name, mode='r'):
    if isinstance(file_or_name, io.IOBase):
      self.file = file_or_name
    else:
      self.file = open(file_or_name, mode)
    return
  def read(self, size=-1):
    return self.file.read(size)
  def write(self, data):
    self.file.write(data)
    return len(data)
  def close(self):
    self.file.close()
    return
  def seek(self, offset, whence=io.SEEK_SET):
    return self.file.seek(offset, whence)
  def tell(self):
    return self.file.tell()
  def fileno(self):
    return self.file.fileno()
  def flush(self):
    self.file.flush()
    return
  def __enter__(self):
    return self
  def __exit__(self, type, value, tb):
    self.close()

