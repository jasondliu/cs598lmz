from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

#lzma, lzmacat
#xz, xzcat

# tar -c <filename(s)> -z -f <name_of_archive>.tar.xz
# tar -c <filename(s)> -j -f <name_of_archive>.tar.bz2
# tar -x -f <name_of_archive>.tar.xz
# tar -x -f <name_of_archive>.tar.bz2
