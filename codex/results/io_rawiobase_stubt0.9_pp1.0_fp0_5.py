import io
class File(io.RawIOBase):
  def __init__(self):
    pass
  def readinto(self, buf):
    if (len(buf) > 5):
      buf[0:5] = b'12345'
    # Let readinto fail due to our output parameters not being 'file like'
    raise IOError()
  def write(self, data):
    pass
  def close(self):
    pass
  def fileno(self):
    pass
  def flush(self):
    pass
  def seek(self, offset, whence=0):
    pass
  def tell(self):
    pass
  def readable(self):
    pass
  def writable(self):
    pass
  def seekable(self):
    pass

class WritableFile(File):
  def readable(self):
    return False
  def writable(self):
    return True
  def seekable(self):
    return True
  def close(self):
    pass

cur_dir = os.path.dirname(os.path.abspath(__file__))

class TestFile
