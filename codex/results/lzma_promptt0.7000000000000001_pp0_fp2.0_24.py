import lzma
# Test LZMADecompressor with a stream of at most 8 bytes
decompressor = lzma.LZMADecompressor(format=lzma.FORMAT_AUTO, memlimit=8)
    
# Decompress the file.
with gzip.open("C:/Users/Sam/Desktop/Harvard/Semester 2/CS 181/Project/Data/train_5.gz", 'rb') as input, open("C:/Users/Sam/Desktop/Harvard/Semester 2/CS 181/Project/Data/train_5.txt", 'wb') as output:
    for line in input:
        output.write(decompressor.decompress(line))

# Flush the decompressor because we are done.
output.write(decompressor.flush())


 
import lzma
# Test LZMADecompressor with a stream of at most 8 bytes
decompressor = lzma.LZMADecompressor(format=lzma.FORMAT_AUTO, memlimit=8)
    
# Decompress the file.
with gzip.open("C:/Users
