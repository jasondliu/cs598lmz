import mmap
# Test mmap.mmap

# Create a file
with open('test.txt', 'w') as f:
    f.write('abcdefghijklmnopqrstuvwxyz')

# Open the file
with open('test.txt', 'r') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

    # Print the first character
    print(m[0])

    # Print the entire file
    print(m[:])

    # Close the mmap
    m.close()

# Delete the file
os.remove('test.txt')
