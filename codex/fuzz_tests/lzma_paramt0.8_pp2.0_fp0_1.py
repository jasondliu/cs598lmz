from lzma import LZMADecompressor
LZMADecompressor().decompress(cf['data']['body']['data'])

from bz2 import BZ2Decompressor

# Create a decompressor object
decompressor = BZ2Decompressor()

# Iteratively decompress the data
decompressed_data = []
while True:
  chunk = cf['data']['body']['data']['data']
  if chunk:
    decompressed_data.append(decompressor.decompress(chunk))
  else:
    break
    
# Concatenate and print the decompressed data
decompressed_data = b''.join(decompressed_data)
print(decompressed_data)
