from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_string)

# We're going to write a function that can decompress a string that's been compressed using the BZ2 compression algorithm. The function should take just one argument, a string that's been compressed using BZ2, and return the decompressed version of that string.

# Instructions
# Write a function called decompress that accepts a single argument, which will be a bytes object.

# Call the bz2.BZ2Decompressor().decompress() method on the argument, and return the result of that.

# Call the decompress() function with the compressed_string from before, and print the result.
