from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# lzma.LZMAError: Input format not supported by decoder
# Reason: The file is not in the .xz format.

# The LZMADecompressor class can only decompress data that has been
# compressed using the .xz file format.

# The .xz format is a single-file compression format that is based on
# the LZMA2 algorithm.

# The .xz format is ideal for packaging and compressing collections of
# files and directories.

# The .xz format is also ideal for compressing short files, such as
# individual text files, and for compressing files that use a small
# number of distinct byte values, such as executable programs.

# The .xz format is not ideal for compressing files that already use a
# compressed file format, such as .zip files and .jpg image files.

# The .xz format is not ideal for compressing files that contain a
# large amount of random data, such as .iso disk images.

# The .xz format is not ideal for compressing files that contain
