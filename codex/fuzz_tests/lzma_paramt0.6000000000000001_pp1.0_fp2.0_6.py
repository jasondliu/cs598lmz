from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

uncompressed_file_size = os.path.getsize(uncompressed_file_path)
uncompressed_file_size

# %%
#
# .. _lzma_stream:
#
# LZMA compression: stream compression
# =====================================
#
# The LZMA compression format supports multiple compression algorithms.
# The most common algorithm used in the .xz format is LZMA2, which is based on
# LZMA but adds support for better data compression.
#
# The LZMA2 format supports a number of features that are not available in the
# simpler LZMA format. One of them is "streaming", which allows data to be
# compressed in chunks.
#
# The LZMA2 format also supports a "preset" option to set the compression level
# of the data. This makes it possible to trade compression ratio for compression
# speed and vice versa.
#
# The following example uses the LZMA2 format to compress a file in chunks.
#
# .. code-block:: python
#
#     import
