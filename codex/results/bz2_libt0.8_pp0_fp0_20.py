import bz2
bz2.decompress(bz2.compress(text, 9))
# bz2.decompress(bz2.compress(text, 9))
print(text)

# The maximum compression level is 9; here are various sizes for the Wikipedia
# article on LZW (compression level 9 creates the smallest file):

import size
size.size_in_bytes('lzw.txt')
# 2492

size.size_in_bytes('lzw.txt.gz')
# 469

size.size_in_bytes('lzw.txt.bz2')
# 467

size.size_in_bytes('lzw.txt.xz')
# 283

size.size_in_bytes('lzw.txt.lzma')
# 283


# #### Modules for command-line scripts

# A command line tool is a program that can be called from the command line.
# Many of the standard Python programs are command line tools. The simplest
# way to get the functionality of such a program is to call it with
# `
