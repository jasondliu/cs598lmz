import mmap
# Test mmap.mmap()

# Create file
with open('test.txt', 'w') as f:
    f.write('Hello world!')

# Open file and map to memory
with open('test.txt', 'r+') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.readline())
    
    # Move to beginning of file
    m.seek(0)
    # Write to file
    m.write(b'Hello world!')

# Close map
m.close()

# Open file and map to memory
with open('test.txt', 'r+') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.readline())

# Close map
m.close()

# Delete file
os.remove('test.txt')

# Test mmap.mmap()

# Create file
with open('test.txt', 'w') as f:
    f.write('Hello world!')

# Open file and map to memory
with open('test.txt
