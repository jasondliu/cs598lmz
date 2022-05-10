import bz2
bz2.BZ2File(filename, "r")  # opens filename, returning a file-like object

# To compress a string
bz2.compress(string)

# To decompress a string
bz2.decompress(string)

# To compress a file
input = open(input_filename, "rb")
output = bz2.BZ2File(output_filename, "wb")
while True:
    data = input.read(1024)
    if not data:
        break
    output.write(data)  # The write() method does the compression
output.close()
input.close()

# To decompress a file
input = bz2.BZ2File(input_filename, "rb")
output = open(output_filename, "wb")
while True:
    data = input.read(1024)
    if not data:
        break
    output.write(data)  # The write() method does the decompression
output.close()
input.close()

"""

"""
5.1.5. zipfile — Work with ZIP
