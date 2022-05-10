import io
class File(io.RawIOBase):
 def close(self):
  pass
 def fileno(self):
  return 0
 def flush(self):
  pass
 def isatty(self):
  return False
 def read(self,n=0):
  data = self.readinto(self.buffer)
  if data:
   return data[0:n]
  else:
   return b''
 def readable(self):
  return True
 def readinto(self,b):
  return 0
 def readline(self,n=0):
  data = self.readinto(self.buffer)
  if data:
   return data[0:n]
  else:
   return b''
 def seek(self,offset,whence=0):
  pass
 def seekable(self):
  return False
 def tell(self):
  return 0
 def writable(self):
  return False
 def write(self,b):
  pass
 def __init__(self,file_name,mode='rb',*args,**kargs):
  self.buffer = bytearray(1024)
  self._
