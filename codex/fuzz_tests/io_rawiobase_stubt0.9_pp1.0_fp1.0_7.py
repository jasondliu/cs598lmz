import io
class File(io.RawIOBase):
   def __init__(self,path,flag=0):
      self.path=path
      self.flag=flag
      if os.path.exists(self.path):
         if flag==0:
            f=open(self.path,"r")
            f.close()
         if flag==1:
            f=open(self.path,"w")
            f.close()
      else:
         raise ValueError("File not Found")
   def __del__(self):
      if os.path.exists(self.path):
         if flag==0:
            f=open(self.path,"r")
            f.close()
         if flag==1:
            f=open(self.path,"w")
            f.close()
   def readline(self):
      if self.flag==0:
         f=open(self.path,"r")
         l=f.readline()
         f.close()
      else:
         raise OSError("File is not open for reading")
      return l
   def write(self,data):
