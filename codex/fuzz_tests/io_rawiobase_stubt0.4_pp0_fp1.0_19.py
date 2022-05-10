import io
class File(io.RawIOBase):
  def __init__(self, path, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
    self.path = path
    self.mode = mode
    self.buffering = buffering
    self.encoding = encoding
    self.errors = errors
    self.newline = newline
    self.closefd = closefd
    self.opener = opener
    self.file = None
    self.pos = 0

  def __enter__(self):
    self.open()
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.close()

  def open(self):
    if self.file is None:
      self.file = open(self.path, self.mode, self.buffering, self.encoding, self.errors, self.newline, self.closefd, self.opener)
      self.pos = self.file.tell()

  def close(self):
    if self.file is not None
