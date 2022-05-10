import mmap
# Test mmap.mmap()

# Open file
f = open('test.txt', 'r+')

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Print file contents
print m.readline()

# Update content and save
m.seek(0)
m.write('0123456789abcdef')
m.write('0123456789abcdef')
m.write('0123456789abcdef')
m.write('0123456789abcdef')
m.write('0123456789abcdef')
m.write('0123456789abcdef')
m.write('0123456789abcdef')
m.write('0123456789abcdef')
m.write('0123456789abcdef')
m.write('0123456789abcdef')
m.write('0123456789abcdef')
m.write('0123456789abcdef')
m.write('0123456789abcdef')
m.write('0123456789abcdef')
m.write('
