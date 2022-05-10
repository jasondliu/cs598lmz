import io
class File(io.RawIOBase):
  def close(self):
    """
    Implements RawIOBase.close().
    """
  def fileno(self):
    """
    Implements RawIOBase.fileno().
    """
  def flush(self):
    """
    Implements RawIOBase.flush().
    """
  def isatty(self):
    """
    Implements RawIOBase.isatty().
    """
  def readable(self):
    """
    Implements RawIOBase.readable().
    """
  def readinto(self, b):
    """
    Implements RawIOBase.readinto().
    """
  def readline(self, limit=-1):
    """
    Implements RawIOBase.readline().
    """
  def seekable(self):
    """
    Implements RawIOBase.seekable().
    """
  def seek(self, offset, whence=0):
    """
    Implements RawIOBase.seek().
    """
  def tell(self):
    """
    Implements Raw
