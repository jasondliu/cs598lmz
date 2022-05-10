import bz2
bz2.BZ2File(filename, mode='w')

# Read the compressed file
with bz2.BZ2File(filename, 'r') as file:
    file_content = file.read()
    print(file_content)

# Write and compress the file content
with bz2.BZ2File(filename, 'w') as file:
    file.write(file_content)

# Read the compressed file
with bz2.BZ2File(filename, 'r') as file:
    print(file.read())

# Read the compressed file
with bz2.BZ2File(filename, 'r') as file:
    print(file.read())

# Read the compressed file
with bz2.BZ2File(filename, 'r') as file:
    print(file.read())

# Read the compressed file
with bz2.BZ2File(filename, 'r') as file:
    print(file.read())

# Read the compressed file
with bz2.BZ2File(filename, 'r') as file
