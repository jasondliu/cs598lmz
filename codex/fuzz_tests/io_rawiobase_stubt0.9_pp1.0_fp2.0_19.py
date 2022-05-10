import io
class File(io.RawIOBase):
  def __init__(self, f):
     self.f = f
  def readinto(self, b):
    n = len(b)
    view = memoryview(b).cast('B')
    while n > 0:
      r = self.f.read(n)
      view[:len(r)] = r
      view = view[len(r):]
      n -= len(r)
      if len(r) == 0:
        break
    return len(b) - n
  def close(self):
    return self.f.close()

def test():
  cwd = b"/root/.local/share/jupyter/runtime/kernel-8f176e95-0ee7-42f8-b25d-b6865c3ac25e"
  sys.path.insert(0,cwd)
  # This is added to syspath by Jupyter, we want to import from this path
  with open("./f1.py","rb") as f:
    max_read = 10
    dyn_module
