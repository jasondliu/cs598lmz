import bz2
# Test BZ2Decompressor
data = open('example.txt.bz2','rb').read()
print(data)

# decompressor = bz2.BZ2Decompressor()
# result = decompressor.decompress(data)
# print(result)

# with bz2.BZ2File('example.txt.bz2') as input:
#     print(input.read())
