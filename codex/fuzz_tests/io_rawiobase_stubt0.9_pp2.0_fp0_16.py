import io
class File(io.RawIOBase):
  def __init__(self, filepath):
    self.filepath = filepath
    self.f = None
  def __enter__(self):
    self.f = open(self.filepath, 'r')
    return self
  def readall(self):
    return self.f.read()
  def __exit__(self,*args):
    if self.f is not None:
      self.f.close()


# The following is the solution file, minus the descriptions.

class LineFile(File):
  def __init__(self, filepath, line, column):
    super().__init__(filepath)
    self.line = line
    self.column = column
  def __enter__(self):
    super().__enter__()
    for l in range(self.line):
      self.f.readline()
    self.f.seek(self.f.tell() + self.column - 1)
    return self
  def readall(self):
    return self.f.read()

class DiffFile(File):
 
