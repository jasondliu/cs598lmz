import lzma
lzma.decompress(data)

# Or you can use it on a file
# with open('file.xz', 'rb') as ix:
#     with open('file.txt', 'wb') as ox:
#         ox.write(lzma.decompress(ix.read()))
