import io
class File(io.RawIOBase):
  def writable(self):
    return True
  def write(self, data):
    print(data)
  def read(self, data):
    return b'0'
f = File()
f.write(b"hello")
f.read(1)
