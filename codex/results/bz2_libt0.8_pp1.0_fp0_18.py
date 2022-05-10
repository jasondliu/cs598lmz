import bz2
bz2_file = bz2.BZ2File('nyc.txt.bz2')
file_content = bz2_file.read()
bz2_file.close()

print(file_content[:100])

# Writing files
with bz2.BZ2File('new_file.txt.bz2', 'w') as f:
    f.write(b'A bunch of text to be compressed')
# Reading the compressed data
with bz2.BZ2File('new_file.txt.bz2', 'r') as f:
    file_content = f.read()

file_content
 
# -- end code --
