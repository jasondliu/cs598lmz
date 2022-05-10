import bz2
bz2.BZ2File(filename)

#The gzip and bz2 modules contain compression methods
#These modules use the same methods to compress and decompress data
#The difference lies in the way they compress the data
#The gzip method compresses every single file into one gzip file
#The bz2 method compresses each file and places it into its own bz2 file

#Compressing multiple files into a single archive is good for backup purposes
#but it is not ideal when you need to access a single file within the backup
#The bz2 method is better for this purpose

#The gzip and bz2 modules provide .open() methods to create file objects
#This is the preferred way to read and write the compressed files
#The .open() method is similar to the built-in open() function

#The .open() method requires a filename and a mode
#The mode argument can be 'r' for reading, 'w' for writing and 'rb' for reading a compressed file
#The default is 'rb'
#You can also pass an argument for the compression level, which must be an integer between 1 and 9
#
