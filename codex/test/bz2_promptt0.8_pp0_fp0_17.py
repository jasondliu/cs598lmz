import bz2
# Test BZ2Decompressor function
#

def main():
    for i in range(1000):
        inp = "Thank you for using the BZIP2 compressor."
        print ("Iteration ",i," : ",sys.getsizeof(inp)," bytes")
        # Compress the bytes using bz2.compress()
        compressed = bz2.compress(inp.encode())
        # Print the size of the compressed output data
        print ("Compressed size is: ", sys.getsizeof(compressed))
        # Decompress the bytes using bz2.decompress()
        decompressed = bz2.decompress(compressed)
        # Extract the original bytes from the decompressed data
        result = decompressed.decode()
        print ("Decompressed data is: ", result)

