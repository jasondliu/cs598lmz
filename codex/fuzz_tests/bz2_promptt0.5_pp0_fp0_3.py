import bz2
# Test BZ2Decompressor
print('%15s %15s' % ('len(data)', 'len(decompressed)'))
print('%15i %15i' % (len(data), len(bz2.decompress(data))))

# Test BZ2File
with open('bz2file_write.bz2', 'wb') as f:
    f.write(data)
with bz2.BZ2File('bz2file_write.bz2', 'rb') as f:
    file_content = f.read()
print('%15s %15s' % ('len(data)', 'len(file_content)'))
print('%15i %15i' % (len(data), len(file_content)))

# Test compress
compressed = bz2.compress(b'This is a test')
print('%15s %15s' % ('len(data)', 'len(compressed)'))
print('%15i %15i' % (len(b'This is a test'), len(compressed)))

# Test decompress
dec
