import lzma
# Test LZMADecompressor

# decompress
decompressor = lzma.LZMADecompressor()

with open('enwik8', 'rb') as input, open('enwik8.decoded', 'wb') as output:
  for block in iter(lambda: input.read(64 * 1024), b''):
    output.write(decompressor.decompress(block))

# with open('enwik8.decoded', 'r') as f:
#   print(f.read(100))

# with open('enwik8', 'rb') as f:
#   print(f.read(100))
#   print(f.read(100))
#   print(f.read(100))
#   print(f.read(100))

# with open('enwik8.decoded', 'rb') as f:
#   print(f.read(100))
#   print(f.read(100))
#   print(f.read(100))
#   print(f.read(100))
#   print(f.read(100))
#   print
