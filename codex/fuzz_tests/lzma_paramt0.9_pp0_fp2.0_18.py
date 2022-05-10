from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
'Hello world!\n'

decompressor = LZMADecompressor()
decompressor.decompress(data)
'Hello world!\n'
decompressor.decompress(bytearray())
b''
decompressor.unused_data
b''
# can decompress data from a file
fileobj = io.BytesIO(data)
decompressor.decompress(fileobj.read(10))

# can decompress with the flush() method
decompressor.flush()
# can use the decompress after calling flush()
decompressor.decompress(b'lzma compressed!')
'Hello world!\nlzma compressed!'
# lzma compression format includes multiple files
data = open('pg1342.txt', 'rb').read()
data_compressed = lzma.compress(data)
len(data_compressed)

data_compressed.split(b'\x00')

decompressor = LZMADecompressor()
decompressor.decompress
