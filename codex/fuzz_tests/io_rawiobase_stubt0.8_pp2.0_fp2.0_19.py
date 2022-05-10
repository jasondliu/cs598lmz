import io
class File(io.RawIOBase):
  def read(self, n=-1):
    return bytes(n)

  def write(self, data):
    return len(data)

fp = File()
fp.read()
fp.write(b'abc')
fp.write('abc')
fp.tell()
fp.seekable()
fp.readable()
fp.writable()
fp.seek(0, 0)
fp.close()
fp.seek(-4, 2)
fp.truncate(0)
fp.fileno()
fp.isatty()
fp.seek(-4, io.SEEK_END)

class Error(io.RawIOBase):
  def read(self, n=-1):
    raise OSError(1)
  def write(self, data):
    raise OSError(1)

fp = Error()
try:
  fp.read()
except OSError as e:
  print(e.errno)

try:
  fp.write(b'abc')
except OSError as e:
  print(e
