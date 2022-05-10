import lzma
lzma.decompress(encoded_data)

# Compressed data is now in file_content
# Let's write it back to a new file, to illustrate writing on the fly (as the compression is happening)
with lzma.open('compressed_file.xz', 'wb', preset=lzma.PRESET_EXTREME) as f:
    f.write(file_content)

# You can now also compress and decompress data using the zlib, gzip and bz2 modules
# The zlib module also provides access to the separate gzip and deflate encoders and decoders
with gzip.open('compressed_file.gz', 'rb') as f:
    file_content = f.read()

# Compressed data is now in file_content
# Let's write it back to a new file, to illustrate writing on the fly (as the compression is happening)
with gzip.open('compressed_file.gz', 'wb', compresslevel=5) as f:
    f.write(file_content)

# You can now also compress and decompress data
