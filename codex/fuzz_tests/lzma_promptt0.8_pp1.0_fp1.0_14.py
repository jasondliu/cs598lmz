import lzma
# Test LZMADecompressor
data = open(sys.argv[1], 'rb').read()
print('%d bytes read' % len(data))

cd = lzma.LZMADecompressor()

# First decompress the first chunk
decompressed_data = cd.decompress(data)
print('%d decompressed bytes' % len(decompressed_data))
print('%d compressed bytes' % cd.unused_data)
data = data[cd.unused_data:]
print('%d compressed bytes after first chunk' % len(data))

# Then decompress the remaining data
decompressed_data += cd.decompress(data, lzma.FORMAT_RAW)
print('%d decompressed bytes' % len(decompressed_data))
print('%d compressed bytes' % cd.unused_data)
data = data[cd.unused_data:]
print('%d compressed bytes after second chunk' % len(data))
</code>
The output of this script with the latest Python 2.7:
<code>C:\Python27&gt;
