import bz2
bz2_file = bz2.BZ2File("../data/train-jpg.tar.bz2")

# Read a chunk of data
chunk = bz2_file.read(100)

# Print out the first 100 bytes
print(chunk)

# Print out the last 100 bytes
print(bz2_file.read(100)[-100:])

# Close the file
bz2_file.close()

# Import tarfile
import tarfile

# Open the file using tarfile.open()
tar = tarfile.open("../data/train-jpg.tar.bz2")

# Print out the members of the tar
print(tar.getmembers())

# Extract the first member using tarfile.extract()
tar.extract(tar.getmembers()[0])

# Close the tarfile
tar.close()

# Import tarfile
import tarfile

# Open the file using tarfile.open()
tar = tarfile.open("../data/train-jpg.tar.bz2")

# Iterate over the members
