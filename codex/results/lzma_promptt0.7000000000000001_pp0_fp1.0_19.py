import lzma
# Test LZMADecompressor.
with lzma.open('test.txt.xz') as f:
	file_content = f.read()

print(file_content)

#compress file
comp = lzma.LZMACompressor()
with open('foo', 'rb') as f_in, open('foo.xz', 'wb') as f_out:
    f_out.write(comp.compress(f_in.read()))
    f_out.write(comp.flush())

#decompress file
decomp = lzma.LZMADecompressor()
with open('foo.xz', 'rb') as f_in, open('bar', 'wb') as f_out:
    f_out.write(decomp.decompress(f_in.read()))
