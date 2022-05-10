import bz2
# Test BZ2Decompressor
decomp = bz2.BZ2Decompressor()

# Decompress our file
data = decomp.decompress(compressed_data)

# Print the decompressed data
print(data)


# In[ ]:


# Create a BZ2File object
bz_file = bz2.BZ2File('Compressed_Wiki.bz2')

# Read the compressed file
file_content = bz_file.read()

# Print the decompressed data
print(file_content)


# In[ ]:


# Open the file for reading
file = open('Compressed_Wiki.bz2', 'rb')

# Create an empty list
lines = []

# Read the file line by line and decompress it
for line in file.readlines():
    lines.append(bz2.decompress(line))

# Print the decompressed data
print(lines)


# In[ ]:


# Print the first 5 lines of the decompressed file
for line in lines[:5]:
    print(line)



