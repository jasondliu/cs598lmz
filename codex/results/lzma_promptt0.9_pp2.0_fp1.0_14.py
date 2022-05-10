import lzma
# Test LZMADecompressor of lzma:
tfile = open('lzma_test.txt', 'wb')
tdata = b'Some data to test LZMA compression.\n'
tfile.write(tdata * 100)
tfile.close()
zipped = lzma.compress(b'1234567890')
with lzma.open('lzma_test.txt.xz', 'wb') as g:
    for i in zipped:
        g.write(i)
g = lzma.open('lzma_test.txt.xz', 'rb')
with lzma.LZMADecompressor() as decomp:
    for s in decomp.decompress(g.read()):
        print(s)
print('Non-context-managed:\n')
decomp = lzma.LZMADecompressor()
print(decomp.decompress(b'1234567890'))
decomp.decomprss(b'1234567890')
!rm lzma_test.txt
!xz -d --
