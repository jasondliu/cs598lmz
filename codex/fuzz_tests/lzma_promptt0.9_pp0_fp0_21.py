import lzma
# Test LZMADecompressor
in_file = open('c:/Users/jeff.reaves/Downloads/test2.tar.lzma', 'rb')
dc = lzma.LZMADecompressor()
out_file = open('testfile.tar', 'wb')
while True:
    chunk = in_file.read(1024)
    if not chunk:
        break
    chunk = dc.decompress(chunk)
    if chunk:
        out_file.write(chunk)
out_file.close()
in_file.close()
</code>

