import bz2
bz2.BZ2File(bz2_file_path, 'w')

# Create a BZ2 file that contains the compressed contents of 'data.csv' and assign it to bz2_file.
bz2_file = bz2.BZ2File(bz2_file_path, 'wb')
bz2_file.write(data)
bz2_file.close()

# Reopen the closed BZ2 file 'bz2_file' and assign the decompressed file contents to 'data_again'.
bz2_file = bz2.BZ2File(bz2_file_path, 'r')
data_again = bz2_file.read()
print(data_again == data)

# Write a function to compress a file using bz2 compression and return the resulting compressed file object.
def bz2_compress(file_name):
    """Compress a file using bz2 compression.

    Positional argument:
    file_name -- a string for the file path of the file to be compressed.
    
    Example:

