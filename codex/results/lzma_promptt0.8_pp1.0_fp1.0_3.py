import lzma
# Test LZMADecompressor against the testdata from xz-java
# see https://github.com/tukaani/xz/tree/master/src/test/resources/lzma

for filename in os.listdir('xz-java/lzma'):
  if not filename.endswith('.lzma'):
    continue
  print(filename)
  with open('xz-java/lzma/' + filename, 'rb') as f:
    compressed = f.read()
  assert(compressed[0:5] == b'\xfd7zXZ\x00')
  with open('xz-java/lzma/' + filename.replace('.lzma', '.txt'), 'rb') as f:
    expected = f.read()
  decomp = lzma.LZMADecompressor()
  got = decomp.decompress(compressed[12:])
  assert(got == expected)

# Test LZMACompressor against the files in xz-java
for filename in os.listdir('xz-java/lzma
