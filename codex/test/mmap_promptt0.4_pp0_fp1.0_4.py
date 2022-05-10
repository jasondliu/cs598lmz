import mmap
# Test mmap.mmap

# Open file
f = open("/dev/mem", "r+b")

# Map the memory
m = mmap.mmap(f.fileno(), 0x1000, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE, 0x10000000)

# Read the memory
print(m[0:0x1000])

# Write to the memory
m[0:0x1000] = b'\x00' * 0x1000

# Close the memory
m.close()

# Close the file
f.close()
