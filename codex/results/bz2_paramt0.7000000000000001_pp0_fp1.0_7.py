from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(decoded_data)

# with open('/home/tushar/Desktop/test.bz2', 'rb') as f:
#     decompressor = BZ2Decompressor()
#     file_content = f.read()
#     data = decompressor.decompress(file_content)
#     print(data)
