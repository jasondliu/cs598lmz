import lzma
# Test LZMADecompressor

## Try to decompress something

s = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_!"#$%&\'()*+,-./:;<=>?@[\\]^_{|}~'
cf = lzma.LZMACompressorFilter()
data = cf.compress(s) + cf.flush()

filename = 'decompressed'
dc = lzma.LZMADecompressor()
with open(filename, 'wb') as f:
    f.write(data)
output = dc.decompress(data)
print(output)

print(output == s)

## Test incomplete or corrupt data

try:
    dc.decompress(data[:-1])
except EOFError as err:
    print('Expected error: %s' % err)

try:
    dc.decompress(b'')
except EOFError as err:
    print('Expected error: %s' % err)

