import mmap
# Test mmap.mmap(0, 1) 
m = mmap.mmap(-1, 1)
print("Before data is added: ", list(m))

# Add data to the mmap object.
m.write('py'.encode())
print("After data is added: ", list(m))

m.seek(0)
m.write('PY'.encode())
print("After data is added: ", list(m))

print("After data is added: ", m.read(1))
print("After data is added: ", m.readline())

# Close the mmap and file objects.
m.close()
print("After close: ", list(m))
