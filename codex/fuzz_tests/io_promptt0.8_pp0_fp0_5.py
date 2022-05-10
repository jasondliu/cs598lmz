import io
# Test io.RawIOBase() if possible; otherwise try io.BytesIO as a fallback.
try:
  testRawIOBase = io.RawIOBase()
  testRawIOBase.fileno()
  testRawIOBase.readable()
  testRawIOBase.writeable()
  testRawIOBase.seekable()
  testRawIOBase.close()
  testRawIOBase.isatty()
  testRawIOBase.tell()
  testRawIOBase.read()
  testRawIOBase.readinto()
  testRawIOBase.readline()
  testRawIOBase.readlines()
  testRawIOBase.write()
  testRawIOBase.writelines()
  testRawIOBase.seek()
  testRawIOBase.truncate()
  testRawIOBase.flush()
except Exception:
  ioRawIOBase = None
else:
  ioRawIOBase = io.RawIOBase
try:
  testBytesIO = io.BytesIO()
  testBytesIO.fileno()
  testBytesIO.readable()
  testBytesIO.writeable()
 
