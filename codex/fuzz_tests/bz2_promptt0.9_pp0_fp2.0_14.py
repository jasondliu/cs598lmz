import bz2
# Test BZ2Decompressor
bz_decompressor = bz2.BZ2Decompressor()
with open('coins.bz2', 'rb') as f:
    file_content = f.read()
    oreo = bz_decompressor.decompress(file_content)
    print(oreo)
# your code
# Show the first 10,000 bytes of the decompressed file
print(oreo[:1000])


# Compare the size of the compressed file to the decompressed file
import os

print(f'Coins decompressed size: {os.path.getsize("coins.txt")}')
print(f'Coins compressed size: {os.path.getsize("coins.bz2")}')


# Show that the file is smaller after compression


# Bonus: What is another use for bzip compression?
# perhaps using bzip compression to stream media data over the Internet.


# Exercise 3:
# Explore the Gzip file format:

# Read in the baby2018.html.gz file


# Show the first 100 bytes of the file


# Show the first 100 bytes
