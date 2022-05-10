import bz2
bz2.BZ2File(path, 'rb')

# Read the file into a list: lines
with bz2.BZ2File(path, 'rb') as file:
    lines = file.readlines()

# Print the first line of lines
print(lines[0])

# Create an iterator for lines: lines_iter
lines_iter = iter(lines)

# Print the first 5 lines of lines_iter
print(next(lines_iter))
print(next(lines_iter))
print(next(lines_iter))
print(next(lines_iter))
print(next(lines_iter))

# Import necessary modules
from io import BytesIO
from zipfile import ZipFile

# Open a zip file in read mode
with ZipFile('my_files.zip', 'r') as z:
    # Print all the contents of the zip file
    z.printdir()

    # Extract all the contents
    z.extractall()

# Open and read zip file
with ZipFile('my_files.zip', 'r') as z:
    for filename in ['
