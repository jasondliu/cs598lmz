import io
class File(io.RawIOBase):
   """
   File I/O in the style of uPy's `uio.IOBase`
   """
   def __init__(self, *args, **kwargs):
      raise NotImplementedError

   def close(self, *args, **kwargs):
      """
      close(self)
      """
      raise NotImplementedError

   def flush(self, *args, **kwargs):
      raise NotImplementedError

   def read(self, *args, **kwargs):
      raise NotImplementedError

   def readinto(self, *args, **kwargs):
      raise NotImplementedError

   def write(self, *args, **kwargs):
      raise NotImplementedError
