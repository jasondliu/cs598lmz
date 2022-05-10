import lzma
lzma.open

# Compression level 1 is the fastest and produces the least compression, while
# 9 is the slowest and produces the most compression. The default is 6.

# The default format is XZ, but the legacy LZMA format can be used by
# specifying format=lzma.FORMAT_ALONE.

# The default filter chain is designed to be compatible with LZMA Utils.
# To change the filter chain, use the filters keyword argument.

# The filters keyword argument must be a sequence of dicts. Each dict must
# have an id key and a props key. The id key specifies the filter ID, and
# the props key specifies the filter properties.

# The filter chain can be modified by adding, removing, or changing the
# properties of filters.

# The default filter chain is:
# [
#     {"id": lzma.FILTER_LZMA2, "preset": 6 | lzma.PRESET_EXTREME},
# ]

# The filter chain can be specified as a list of dicts, or as a list of
# tuples. The
