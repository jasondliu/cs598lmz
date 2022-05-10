from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open(TAR_BZ_PATH, 'rb').read())

# CONCLUSION: 
# TAR_Z_PATH -> uncompressed size: 940 MB
# TAR_GZ_PATH -> uncompressed size: 582 MB
# TAR_BZ2_PATH -> uncompressed size: 582 MB

# INSTRUCTIONS: 
# Create a file <your_user_name>_assignment8.py
# Import tarfile and bz2 modules
# Create a tarfile object and assign it to tar_file
# Call the extractall() method with appropriate arguments on tar_file
# Create a BZ2Decompressor object and assign it to bz2_decompressor
# Decompress the data with bz2_decompressor
# Assign the result to data
# Print the first 100 bytes of data
# Close the tar_file
# Note: You should not need to use with to create any file objects in this exercise

import tarfile
import bz2
tar = tarfile.open(TAR_GZ_PATH)
tar.extractall
