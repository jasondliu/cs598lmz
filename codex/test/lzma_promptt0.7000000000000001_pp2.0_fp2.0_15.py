import lzma
# Test LZMADecompressor
# https://stackoverflow.com/questions/3585053/python-lzma-library-and-extracting-single-files-from-xz-files
decompressor = lzma.LZMADecompressor()
filename = 'train.csv.xz'
