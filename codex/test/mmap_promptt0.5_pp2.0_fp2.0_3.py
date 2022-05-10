import mmap
# Test mmap.mmap.flush()

# Create a file large enough to map
with open("hello.txt", "wb") as f:
    f.seek(1024**2)
    f.write(b"\0")

with open("hello.txt", "r+b") as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b"hello")
    m.seek(0)
    m.flush()
    assert m.read(5) == b"hello"
    m.close()
print("mmap.flush() test passed.")
