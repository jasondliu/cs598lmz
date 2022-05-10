import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed)

# Decompress the entire file
with bz2.open(filename, 'rt') as file:
    decompressed_data = file.read()
    # decompressed_data = decompressor.decompress(file.read()) # read in compressed data
    
print(decompressed_data[:200])

# <script.py> output:
#     b'\nBZh91AY&SY\xab\xa8@\xd4\x15\xba\xbc\x8c\x05/\x1b\xab\xa8@\xd4\x15\xba\xbc\x8c\x05\x1b\xab\xa8@\xd4\x15\xba\xbc\x8c\x05\x1b\xab\xa8@\xd4\x15\xba\xbc\x8c\x05\x1b\xab\xa8@\xd
