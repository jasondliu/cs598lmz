import lzma
# Test LZMADecompressor object
data = b'Hello, world!'
d = lzma.LZMADecompressor()
d.decompress(data)
d.decompress(b'')  # EOF
d.decompress(b'x')  # raise LZMAError because format error
# Test LZMAFile object
if sys.platform == 'win32':
    # On Windows, lzma module does not support opening file in mode 'U'
    # for binary files
    mode_u = ''
else:
    mode_u = 'U'

f = lzma.LZMAFile(io.BytesIO(data))
f.read()
f.read()
f.seek(0)
f.read()

f = lzma.LZMAFile(io.BytesIO(data), 'r')
f.read()
f.read()
f.seek(0)
f.read()

f = lzma.LZMAFile(io.BytesIO(data), 'rb')
f.read()
f.read()
f.seek
