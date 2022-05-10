import lzma
# Test LZMADecompressor`
# decompressor = lzma.LZMADecompressor()
# decompressed_data = decompressor.decompress(compressed_data)
# print(decompressed_data.decode())

# Real decompress
# with open(r'e:\workspace\pythondl\data\rawdata', 'rb') as f:
#     uncompressed = b''
#     for i in range(0, 3):
#         compressed = f.read(500000)
#         uncompressed += lzma.decompress(compressed)
#     with open(r'e:\workspace\pythondl\data\rawdata.txt', 'wb') as g:
#         g.write(uncompressed)

# Get unicode string
# with open(r'e:\workspace\pythondl\data\rawdata', 'rb') as f:
#     uncompressed = b''
#     while True:
#         try:
#             compressed = f.read(500000)
#             uncompressed += lzma.decompress(comp
