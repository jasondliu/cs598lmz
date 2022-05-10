import lzma
# Test LZMADecompressor
# If you want to test this code on your machine, please uncomment the below line
# compressor = lzma.LZMADecompressor()
# data = b"XXXXX"  # data that is compressed. "XXXXX" is data that has been compressed.
# out = b"XXXXX"  # where the data gets output to.
# compressor.decompress(data, out)
# print(out)  # prints the uncompressed data.

"""
The basic steps will look something like this:
1) We initialize a decompressor by creating an instance of lzma.LZMADecompressor
2) Then we set some data that is compressed or has been compressed, which we will be passing as an argument.
3) Then we initialize an "out" variable, which sets an output for the data that is decompressed.
4) Then we call the decompress method on the decompressor object, passing the data and out variables as arguments.
5) Finally, we print out the out variable to get the decompressed data. 
"""
 
"""
Read lzma compressed file
"""
# Reading LZ
