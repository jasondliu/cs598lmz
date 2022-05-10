import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
ct = decompressor.decompress(compressed_data)
print(ct.decode('utf-8'))

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
compressed_data = compressor.compress(data2.encode('utf-8'))
compressed_data += compressor.flush()
print(compressed_data)

# bz2.open(file[, mode, compresslevel])
# mode: 'r' read-only, 'w' write, 'x' create or error, 't' text, 'b' binary
# compresslevel: 1-9
# return a BZ2File object, which is compatible to BufferedIOBase and TextIOBase
# should use open in binary mode, as BZ2File provides no translation from '\n' to '\r\n'
# supports seek, read, write and tell methods
with bz2.open('compressed_file.bz2', 'wt') as f:
    f.write(data
