import lzma
lzma.decompress(inp[8:])

# Unfortunately it's not working for the archive, we need to patch it.
# So I simply used an online LZMA decompressor
# to get the decompressed archive at http://archive.org/download/flag_archive/flag_archive
# That file contains two directories: good and bad.
# The flag is in one of the files of good/ as the name of a file in bad/ indicates.
#
# Flag: FLAG-Uq3qjo6aHEHpzrf0iMFO
