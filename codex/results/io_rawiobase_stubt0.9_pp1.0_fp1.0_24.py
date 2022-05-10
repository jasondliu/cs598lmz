import io
class File(io.RawIOBase):
  def __init__(self, zipfile, zipinfo):
    self.fileobj = zipfile.open(zipinfo)
    self.size = zipinfo.file_size
  
  def readable(self):
    return True
  
  def seekable(self):
    return True
  
  def seek(self, offset, whence=0):
    if whence == 0:
      self.fileobj.seek(offset)
    elif whence == 1:
      self.fileobj.seek(self.fileobj.tell() + offset)
    elif whence == 2:
      self.fileobj.seek(self.size + offset)
    
  def tell(self):
    return self.fileobj.tell()
  
  def read(self, size=-1):
    return self.fileobj.read(size)
  
  def close(self):
    self.fileobj.close()



class ZipPackage(Package):
  def __init__(self, path):
    super().__init__()
    self.zipfiles = []
    
    with zip
