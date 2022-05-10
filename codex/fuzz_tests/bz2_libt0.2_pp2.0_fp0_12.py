import bz2
bz2.decompress(bz2.compress(b'Hello World!'))

# bz2.compress() and bz2.decompress() both return bytes objects.

# The compress() function works best on data that is similar to what you might find in a tar file.
# For example, if you are compressing log files, you’ll get much better compression if you first
# concatenate all the log files together into one big file and then compress the result.

# The bz2 module includes a command-line tool for working with bzip2 files.
# For example, to compress a file, you can run this:
# $ python3 -m bz2 -c originalfile.txt > compressedfile.bz2
# To decompress, you can use this:
# $ python3 -m bz2 -d compressedfile.bz2 > originalfile.txt

# The bz2 module is not capable of directly reading and writing compressed files.
# Instead, it provides a very high-level interface for working with bzip2 compression.
# If you need to compress data one chunk at a
