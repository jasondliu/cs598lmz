import lzma
lzma.decompress(lzma.compress('Hello World!'))

# lzma.decompress(file_object[, format, memlimit, filters])
# lzma.decompress(data[, format, memlimit, filters])
# lzma.decompress(input, output[, format, memlimit, filters])

# decompress using raw data, using decompressor with max memory 2**40
lzma.decompress(compressed_data, format=FORMAT_XZ, memlimit=2**40)

# decompress using file object, using decompressor with max memory 2**40
lzma.decompress(fileobj, format=FORMAT_XZ, memlimit=2**40)

# decompress using file object, use decompressor with max memory 2**20
# and decompress using raw data, using decompressor with max memory 2**40
lzma.decompress(fileobj, fileobj, format=FORMAT_RAW, memlimit=2**20, filters=[{"id": lzma.FILTER_LZMA2
