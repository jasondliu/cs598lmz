import io
class File(io.RawIOBase):
  def __init__(self, f=None, close=None):
    self.name = self.mode = None
    if close is None:
      self.close = f.close
    else:
      self.close = close
    self._file = f

  def close(self):
    pass

  def __enter__(self):
    return self

  def __exit__(self, *exc_info):
    self.close()

  def write(self, b):
    self._file.write(b)

class Link(File):
  def __init__(self, f=None, close=None):
    super(Link, self).__init__(f=f, close=close)
    self._file = f

def op(name, *args):
  try:
    return globals()[name](*args)
  except Exception as e:
    raise e


def open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True, opener=None):
  return op('_
