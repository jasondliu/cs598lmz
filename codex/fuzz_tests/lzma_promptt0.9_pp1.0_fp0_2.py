import lzma
# Test LZMADecompressor implementation

r = lzma._lzma.LZMADecompressor()

def decompress_safe(buf):
  try:
    return r.decompress(buf)
  except lzma.LZMAError:
    return b""

data = b"".join(b"This is test %d." % d for d in range(100))
with lzma.open("testdata.lzma") as f:
  assert f.read() == data
  # Decompress
  f.seek(0)
  d = f.read(1000)
  res = []
  while d:
    res.append(decompress_safe(d))
    d = f.read(1000)
  assert b"".join(res) == data
  f.seek(0)
  # Partial decompress
  res = []
  while True:
    d = f.read(1000)
    if not d:
      break
    res.append(decompress_safe(d))
  assert b"".join(res) == data

