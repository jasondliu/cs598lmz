import lzma
# Test LZMADecompressor of lzma:
tfile = open('lzma_test.txt', 'wb')
tdata = b'Some data to test LZMA compression.\n'
tfile.write(tdata * 100)
tfile.close()
zipped = lzma.compress(b'1234567890')
