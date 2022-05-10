import mmap
# Test mmap.mmap(fileno, length=0)

filename = os.path.join(os.path.dirname(__file__), 'mmap_file')
f = open(filename, 'wb+')

f.write(bytes(bytearray(range(256))))

with mmap.mmap(f.fileno(), 0) as m:
    print(m[:5])
    print(m[5:10])

f.close()

# Clean up if we created the file
if filename != 'mmap_file':
    os.remove(filename)
