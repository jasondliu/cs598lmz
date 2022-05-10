import bz2
bz2.decompress(compressed_data)

## 9. Generating Compressed Files ##

import bz2
uncompressed_file = open("decrypted.bin", "rb")
compressed_file = bz2.BZ2File("compressed.bz2", "wb")
compressed_file.write(uncompressed_file.read())
uncompressed_file.close()
compressed_file.close()

## 10. Iterating Over compressed Files ##

import bz2

for line in bz2.BZ2File("compressed.bz2"):
    print(line)

## 11. Reading from a Compressed File ##

import bz2
bz2_file = bz2.BZ2File("compressed.bz2")
print(bz2_file.readline())
print(bz2_file.readline())
bz2_file.close()

## 12. Extracting Data from JSON ##

# We've created a file, tweets.txt,
# which contains data from Twitter.
import
