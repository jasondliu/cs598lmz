import io
class File(io.RawIOBase):
  def __init__(self, pcloud):
    self._pcloud = pcloud
    self._file = None
    self._filename = ""
    self._filesize = 0
  
  def open(self, filename):
    if self._file:
      return 0
    self._file = open(filename,  "wb")
    if not self._file:
      return 0
    self._filename = filename
    return 1
    
  def fileno(self):
    if not self._file:
      self._file = open(self._filename, "wb")
    if self._file:
      return self._file.fileno()
    return 0
  
  def close(self):
    if self._file:
      self._file.close()
      self._file = None
    
  def readable(self):
    return False
  
  def writeable(self):
    return True
  
  def read(self, n):
    raise io.UnsupportedOperation("Not ready for reading")
  
  def write(self, data):
    if self._file
