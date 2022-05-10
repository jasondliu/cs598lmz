import io
class File(io.RawIOBase):
 def close(self):
  pass
 def fileno(self):
  return 0
 def flush(self):
  pass
 def isatty(self):
  return 0
 def write(self,s):
  return len(s)
 def writelines(self,l):
  return len(l)
io.RawIOBase.close=io.IOBase.close
io.RawIOBase.flush=io.IOBase.flush
io.RawIOBase.writelines=io.IOBase.writelines
b''
b''
 class StringIO(io.TextIOBase):
  def close(self):
   pass
  def flush(self):
   pass
  def getvalue(self):
   pass
  def read(self,n=-1):
   return b''
  def readline(self,length=None):
   return b''
  def readlines(self,sizehint=None):
   return[b'']
  def seek(self,pos):
   pass
  def tell(self):
   return 0
  def truncate(self,size=None):
