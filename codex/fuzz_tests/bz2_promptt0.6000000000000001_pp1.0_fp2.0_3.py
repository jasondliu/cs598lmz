import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

# Read the compressed file
with open("data/wiki.txt.bz2") as file:
    compressed_data = file.read()
    # Decompressed data
    data = decompressor.decompress(compressed_data)
    # Write data
    with open('data/wiki_decompressed.txt', 'wb') as f:
        f.write(data)
        f.close()

# How to open a file in python
# https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
 
file = open("data/wiki_decompressed.txt", "rb")

# Read the first line from the file
print(file.readline())

# Read the second line from the file
print(file.readline())

# Read the rest of the file
print(file.read())

# Close the file
file.close()

# How to open a file in Python
# https://www.pythonforbeginners.com/
