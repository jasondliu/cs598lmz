import io
class File(io.RawIOBase):
  """A file-like object that reads and write to the STDIN and STDOUT pipes of a subprocess.
  """
  def __init__(self, process, encoding=None, errors=None):
    self.process = process
    self.encoding = encoding
    self.errors = errors
    self.stdin_pipe = process.stdin
    self.stdout_pipe = process.stdout

  def readable(self):
    return True

  def writable(self):
    return True

  def seekable(self):
    return False

  def readinto(self, b):
    if self.closed:
      raise ValueError('I/O operation on closed file.')
    read_bytes = self.stdout_pipe.readinto(b)
    if read_bytes == 0:
      return None
    return read_bytes

  def write(self, b):
    if self.closed:
      raise ValueError('I/O operation on closed file.')
    self.stdin_pipe.write(b)
    return len(b)

  def close(self
