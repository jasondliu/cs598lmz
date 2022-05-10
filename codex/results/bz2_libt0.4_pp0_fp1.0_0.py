import bz2
bz2.decompress(bz2data)

# Use the bz2 module to compress a string
bz2.compress(mystring)

# Use the bz2 module to compress a file
bz2.compress(myfile)

# Use the bz2 module to decompress a file
bz2.decompress(myfile)

# Use the bz2 module to decompress a file and save it to a different file
bz2.decompress(myfile, myfile2)

# Use the bz2 module to compress a string into a file
bz2.compress(mystring, myfile)

# Use the bz2 module to compress a file into a file
bz2.compress(myfile, myfile2)

# Use the bz2 module to decompress a file into a file
bz2.decompress(myfile, myfile2)
