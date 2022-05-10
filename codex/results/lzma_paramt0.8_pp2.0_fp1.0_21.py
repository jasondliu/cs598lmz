from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# ERROR
# print(LZMADecompressor().decompress(data))

# Compressed data:
#
# 100000 iterations, 16 bytes each
#     Compress time:    0.6320578575134277
#     Decompress time:  0.006733179569244385
#
# 100000 iterations, 256 bytes each
#     Compress time:    2.4628703594207764
#     Decompress time:  0.032458651065826416
#
# 100000 iterations, 1024 bytes each
#     Compress time:    14.194432258605957
#     Decompress time:  0.22932415008544922
#
# 100000 iterations, 8192 bytes each
#     Compress time:    92.25410223007202
#     Decompress time:  1.5218939781188965
#
# Uncompressed data:
#
# 100000 iterations, 16 bytes each
#     Compress time:    0.1790
