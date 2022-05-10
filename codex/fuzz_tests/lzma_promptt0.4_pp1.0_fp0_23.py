import lzma
# Test LZMADecompressor

# Create a test file
with open('test.txt', 'w') as f:
    f.write('test' * 100)

# Compress the file
with open('test.txt', 'rb') as f_in, lzma.open('test.txt.xz', 'wb') as f_out:
    f_out.writelines(f_in)

# Decompress the file
with lzma.open('test.txt.xz') as f_in, open('test.out', 'wb') as f_out:
    for line in f_in:
        f_out.write(line)

# Check that the output file is correct
with open('test.out', 'rb') as f:
    print(f.read() == b'test' * 100)

# Cleanup
os.remove('test.txt')
os.remove('test.txt.xz')
os.remove('test.out')

# Output: True
</code>

