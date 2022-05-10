import bz2
bz2.decompress(data)

# Create a file object
file = open('file.txt','w')
file.write('This is a new file.')
file.close()

# Read a file object
file = open('file.txt','r')
file.read()

# Append to a file object
file = open('file.txt','a')
file.write(' This is an appended line.')
file.close()

# Delete a file object
import os
os.remove('file.txt')

# Create a directory
os.mkdir('new_dir')

# Create a subdirectory
os.mkdir('new_dir/sub_dir')

# Change working directory
os.chdir('new_dir')

# Remove a directory
os.rmdir('sub_dir')
os.rmdir('new_dir')

# List directory contents
os.listdir('.')

# Get current working directory
os.getcwd()

# Get directory contents
os.listdir('.')
