import bz2
# Test BZ2Decompressor

data = bz2.BZ2File('data/sample.bz2').read()

decompressor = bz2.BZ2Decompressor()

result = decompressor.decompress(data)

print(len(result))

print(result[:100])

print(result[-100:])

print(result.decode('utf-8'))

print(result.decode('utf-8')[:100])

print(result.decode('utf-8')[-100:])

print(result.decode('utf-8')[:100].encode('utf-8'))

print(result.decode('utf-8')[-100:].encode('utf-8'))

print(result.decode('utf-8')[:100].encode('utf-8') == result[:100])

print(result.decode('utf-8')[-100:].encode('utf-8') == result[-100:])

print(result.decode('utf-8')[
