import bz2
bz2_file_path = './data/bz2_file.bz2'

# Create a BZ2File with mode 'w' to write compressed data.
with bz2.BZ2File(bz2_file_path, 'w') as fout:
    fout.write('Contents of the example file go here.\n')
    fout.write('And a second line.')

# Reopen the file with mode 'r' to read the compressed data.
with bz2.BZ2File(bz2_file_path, 'r') as fin:
    print('Entire file:')
    all_data = fin.read()
    print(all_data)

    print('Three characters from the middle:')
    some_data = fin.read(3)
    print(some_data)

    print('The rest of the file:')
    remaining_data = fin.read()
    print(remaining_data)

# The BZ2File class provides a context manager that makes sure the file is properly closed.
with bz2.B
