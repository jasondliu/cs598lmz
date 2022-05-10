from lzma import LZMADecompressor
LZMADecompressor()

print()
print('*' * 28, 'COMPRESSION', '*' * 28)
print()

lzma = lzma.LZMAFile(__file__)
#
# # print(lzma.read())
#
# # print(lzma.fileno())

print()
print('*' * 28, 'HIGH LEVEL INTERFACE', '*' * 28)
print()

print(lzma.close(True))

print()
print('*' * 28, 'LOW LEVEL (FILTERS)', '*' * 28)
print()

# alpha = lzma.FILTERS_ALPHA

lzma_filter = LZMAFilter(action=lzma.FILTER_LZMA1)
lzma_filter = LZMADecompressor()


# print(lzma_filter.deflate())
print(lzma_filter.flush())

encoder = lzma.LZMACompressor()
print(encoder)

print(lzma.
