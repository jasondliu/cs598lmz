import _struct

# The structure of the data file is:
#
# a header with the sizes of 
#
# header format:
#
# * 4 byte integer n, the number of images
# * 4 byte integer r, the height of the images
# * 4 byte integer c, the width of the images
#
# for each of the n images m:
#
# * r*c bytes, representing the image as a raw array of
#   pixels in row major order with no padding between rows
#   and in gray-scale with unsigned char pixels
#
# * 2 byte integer l, the label for the image, one byte per
#   byte of the integer
#
# the header is the first struct.calcsize(fmt) bytes of the
# file, where fmt is the format string specified below
#
# num_labels is the number of distinct labels in the
# dataset
#
# '>' means big endian, 'I' means unsigned integer,
# 'B' means unsigned char
