import lzma
lzma.open(filename, mode='rb')

# lzma.open(filename, mode='rb', preset=9 | lzma.PRESET_EXTREME)

# lzma.open(filename, mode='rb', format=lzma.FORMAT_XZ)

# lzma.open(filename, mode='rb', format=lzma.FORMAT_ALONE)

# lzma.open(filename, mode='rb', filters=[
#     {"id": lzma.FILTER_LZMA2, "preset": 9 | lzma.PRESET_EXTREME},
#     {"id": lzma.FILTER_DELTA, "dist": 5},
# ])
