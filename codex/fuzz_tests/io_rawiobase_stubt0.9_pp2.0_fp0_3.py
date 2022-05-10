import io
class File(io.RawIOBase):
 def __init__(self, file, *args, **kwargs):
  self._file = file
  self._io = io.BytesIO()
  self.closed = False
 def close(self):
  if self.closed:
   return
  self.closed = True
  self._file.write(self.getvalue())
  self._file.close()
 def fileno(self):
  return self._file.fileno()
 def isatty(self):
  return self._file.isatty()
 def __getattr__(self, attr):
  if attr in ('_file','_io','closed','getvalue'):
   raise AttributeError(attr)
  return getattr(self._file, attr)

def set_file(file):
 global stdout,stderr
 orig_stdout = sys.stdout
 orig_stderr = sys.stderr
 try:
  sys.stdout = stdout = File(file,'w')
  sys.stderr = stderr = File(file,'w')
 except:
 
