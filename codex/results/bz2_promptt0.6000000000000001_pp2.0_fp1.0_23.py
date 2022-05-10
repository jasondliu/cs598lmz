import bz2
# Test BZ2Decompressor
#
# This example reads a small file that was compressed with the bz2 module.
# It uses a BZ2Decompressor object to decompress the data.

# A small sample file
sample_file = "sample.bz2"

# Open the compressed file
with bz2.BZ2File(sample_file, "r") as f:

    # Create decompression object
    dec = bz2.BZ2Decompressor()

    # Read compressed data
    compressed = f.read()

    # Decompress data
    uncompressed = dec.decompress(compressed)

    # Print the uncompressed data to the screen
    print (uncompressed.decode("utf-8"))

# gzip
import gzip
# Test gzip
#
# This example reads a small file that was compressed with the gzip module.
# It uses a GzipFile object to decompress the data.

# A small sample file
sample_file = "sample.gz"

# Open the compressed file
with gzip.GzipFile(sample_file, "r")
