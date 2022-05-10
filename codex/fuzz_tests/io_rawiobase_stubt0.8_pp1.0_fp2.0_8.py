import io
class File(io.RawIOBase):
  def __init__(self, filename, mode):
    self._filename = filename
    self._mode = mode
    self._stream = open(filename, mode)
  def readinto(self, b):
    return self._stream.readinto(b)
  def write(self, b):
    return self._stream.write(b)
  def close(self):
    self._stream.close()
  @property
  def mode(self):
    return self._mode
  @property
  def name(self):
    return self._filename
  @property
  def closed(self):
    return self._stream.closed
import os
BINARY_TYPES = (bytes, bytearray, memoryview)
is_binary = lambda s: isinstance(s, BINARY_TYPES)

def is_file(f):
  return isinstance(f, File) or (hasattr(f, 'read') and hasattr(f, 'write'))
class Files(dict):
  def __init__(self, **kwargs):
    super().__
