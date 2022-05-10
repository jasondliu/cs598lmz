import lzma
# Test LZMADecompressor
compressed_data = open("alice29.txt", "rb").read()
compressed = lzma.LZMADecompressor(lzma.FORMAT_AUTO, None, 0)
decompressed = compressed.decompress(compressed_data)
print(decompressed)

# Convert raw bytes to string
my_binary = b'Hello\x06\xf3\xe2\n'
my_string = my_binary.decode()
print(my_string)
another_string = my_binary.decode('latin')
print(another_string)

# Write Byte Arrays
import io
import lzma

output = io.BytesIO()
with lzma.open("alice29.txt", "wb") as output:
    output.write(my_binary)
   
# Read Byte Arrays
import io
import lzma

input_file = lzma.open("alice29.txt")
my_bytes = input_file.read()

"""
Iterators
"""
print('*************************** Iterators
