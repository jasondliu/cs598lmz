import mmap
# Test mmap.mmap.find()
test_file = 'find.txt'
test_string = b'This is a test string for find.'

# Write the text to the file
with open(test_file, 'wb') as f:
    f.write(test_string)

# Open the file
with open(test_file, 'r+b') as f:
    # Memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # Search for a string
    # -1 means "until the end of the mmap"
    print(mm.find(b'test', 0, -1))

<code>Output:
18
</code>

