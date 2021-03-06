from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_data)

#reading files
#open() returns a file object, and is most commonly used with two arguments
f = open('workfile', 'w')
#the first argument is a string containing the filename.
#The second argument is another string containing a few characters describing the way in which the file will be used.
#mode can be 'r' when the file will only be read,
#'w' for only writing (an existing file with the same name will be erased),
#and 'a' opens the file for appending;
#any data written to the file is automatically added to the end.
#'r+' opens the file for both reading and writing.
#The mode argument is optional; 'r' will be assumed if it’s omitted.

#Normally, files are opened in text mode, that means, you read and write strings from and to the file, which are encoded in a specific encoding.
#If encoding is not specified, the default is platform dependent (see open()).
#'b' appended to the mode opens the file in binary mode: now the data is read and written in the
