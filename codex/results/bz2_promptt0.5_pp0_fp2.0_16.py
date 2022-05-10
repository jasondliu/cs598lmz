import bz2
# Test BZ2Decompressor

dec = bz2.BZ2Decompressor()
dec.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# Test BZ2File

with bz2.BZ2File('test.bz2', 'wb') as fout:
    fout.write(b'hello world')

with bz2.BZ2File('test.bz2', 'rb') as fin:
    print(fin.read())

# Test BZ2Compressor

com = bz2.BZ2Compressor()
com.compress(b'hello world')
com.flush()

# Test open

with bz2.open('test.bz2', 'wb') as fout:
    fout.write(b'hello
