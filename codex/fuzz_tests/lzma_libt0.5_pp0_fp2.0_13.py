import lzma
lzma.decompress(lzma.compress('Hello world!'))

# lzma.compress() and lzma.decompress() are the only functions you need for basic LZMA compression.

# Compression levels
# LZMA compression has a single parameter, level, which determines how the compression algorithm will trade speed for compression ratio.
# The default is 6, which is a good compromise between speed and compression ratio.
# The value 9 will use the most CPU time to compress the data, but will give the highest compression ratio.
# The value 1 will use the least CPU time, but will give the lowest compression ratio.
# The value 0 will disable compression.
# The value 10 will use the most CPU time to compress the data and will produce the smallest output, but will be the slowest to compress.

# Compression filters
# LZMA compression can be further customized by specifying a list of filters to be applied to the data before compression.
# Each filter is a tuple of (id, options), where id is the filter ID and options is a bytes object containing the filter options.
# The filter options are filter-specific and are
