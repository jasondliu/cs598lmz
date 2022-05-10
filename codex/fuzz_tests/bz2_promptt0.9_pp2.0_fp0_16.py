import bz2
# Test BZ2Decompressor on small string

file = bz2.BZ2File(os.path.join(get_data_home(), 'test.bz2'))
file.read(10) == b'\x42\x5a\x68\x36\x34\x2d\x31\x31\x00\x00'
file.seek(0)

decomp = bz2.BZ2Decompressor()
decomp.decompress(file.read(10)) == b'BZh6'
decomp.flush() == b'\x31\x31\x00\x00'
file.close()

# Test BZ2File.read()

file = bz2.BZ2File(os.path.join(get_data_home(), 'test.bz2'))
file.read(100) == b'BZh91AY&SY\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3
