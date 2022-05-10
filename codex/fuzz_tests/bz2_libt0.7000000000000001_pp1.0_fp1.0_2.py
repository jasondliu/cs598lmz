import bz2
bz2.compress(text)

# The result is a binary string that is typically around 60% of the original.

# The bz2 module also provides a decompression function:

bz2.decompress(_)

# ### Compressing and Decompressing Files

# The bz2 module includes a BZ2File class for reading and writing compressed files.

# Open the file for writing to with the bz2 compression.

f_out = bz2.BZ2File('test.bz2', 'w')

# Now you can write to it.

f_out.write(text)

# Close the file when you are done.

f_out.close()

# Open the file for reading.

f_in = bz2.BZ2File('test.bz2', 'r')

# Read the contents.

f_in.read()

# Close the file when you are done.

f_in.close()


# ## 6.13. Reading and Writing Compressed Datafiles

# Another option for working with compressed files
