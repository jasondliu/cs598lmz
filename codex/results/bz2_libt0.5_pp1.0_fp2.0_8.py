import bz2
bz2_file = bz2.BZ2File('example.bz2')
print(bz2_file.read())

# Closing the file
bz2_file.close()

# Compressing data
with open('example.txt', 'rb') as input:
    with bz2.open('example.bz2', 'wb') as output:
        output.writelines(input)

# Compressing data with a different compression level
with open('example.txt', 'rb') as input:
    with bz2.open('example.bz2', 'wb', compresslevel=9) as output:
        output.writelines(input)
