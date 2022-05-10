import lzma
# Test LZMADecompressor
data = open('xzfiles/cantrbry.txt.lzma', 'rb').read()
lz = lzma.LZMADecompressor()
t1 = time.time()
txt = lz.decompress(data)
t2 = time.time()
print("Elapsed time for decimal compression: {}ms".format((t2-t1)*1000))
txt = txt.decode('utf-8')
print(txt)
