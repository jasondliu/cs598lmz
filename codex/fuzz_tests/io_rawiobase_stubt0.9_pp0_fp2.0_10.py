import io
class File(io.RawIOBase):
  def __init__(self):
    super().__init__();
    self._writeData=[];
    self.readBuf=[];
    self.readBufPos=0;
    self.explicitClose=False;
    self.closed=False;
    self.pos=0;

  def isatty(self):
    return False;

  def tell(self):
    return self.pos;

  def seekable(self):
    return True;

  def seek(self, myoff, whence=0):
    if whence == 0:
      self.readBufPos = myoff;
    elif whence == 1:
      self.readBufPos = self.readBufPos #maybe should be fixed up
      self.readBufPos += myoff;
    elif whence == 2:
      self.readBufPos = len(self._writeData) + myoff;

  def fileno(self):
    pass;

  def flush(self):
    pass;
  def __del__(self):
    pass;

  def readable(self
