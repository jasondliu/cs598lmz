import mmap
# Test mmap.mmap
with open("test.bin", "wb") as f:
    # Initialize empty bytes
    data = bytes(range(101))
    f.write(data)

print("Test write")
with open("test.bin", "r+b") as f:
    print("Initial state of file")
    with mmap.mmap(f.fileno(), 0) as m:
        print(m.read(101).hex())
    # Modify first byte
    f.read(1)
    f.write(b"\x00")

print("\nTest modification")
with open("test.bin", "r+b") as f:
    print("State of file after modification")
    with mmap.mmap(f.fileno(), 0) as m:
        print(m.read(101).hex())
