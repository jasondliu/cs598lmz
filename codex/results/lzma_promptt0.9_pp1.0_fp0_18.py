import lzma
# Test LZMADecompressor module of lzma module. 
cdata = b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00\x21\x01\x16\x00\xff\xfb\x50\xc4\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
with lzma.LZMADecompressor() as dec:
    text = dec.decompress(cdata)
    print('Decompress by LZMADecompressor().decompress():', text.decode('utf-8'))
# Test LZMAFile module of lzma module.
with lzma.LZMAFile(BytesIO(cdata)) as f:
    text = f.read()
    print('Decompress by LZMAFile():', text.decode('utf-8'))

import bz2
# Test BZ2Decompressor module of
