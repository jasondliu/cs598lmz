import io
class File(io.RawIOBase):
 def __init__(self, name):
  self.f = open(name, 'rb')
  self.name = name
 def readable(self):
  return True
 def seek(self, offset, whence=io.SEEK_SET):
  self.f.seek(offset, whence)
 def read(self, n=-1):
  return self.f.read(n)
 def close(self):
  self.f.close()

def escape(d):
 if isinstance(d, str):
  return encode(d)
 elif isinstance(d, bytes):
  return bytes(d)
 elif isinstance(d, ttypes.Channel):
  return encode(d.title) + b'\x00' + d.first + b'\x00' + d.last + b'\x00' + d.previous + b'\x00'
 elif isinstance(d, ttypes.Peer):
  return d.user_id.to_bytes(8, 'big')
 elif isinstance(d, ttypes.User):
  return (
