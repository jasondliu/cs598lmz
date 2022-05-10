import mmap
# Test mmap.mmap.read_byte()

with open("data/mmap.txt", "rb") as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

    print("Byte:")
    for i in range(10):
        print(m.read_byte(), end=" ")
    print()

    print("\nCharacter:")
    for i in range(10):
        print(m.read_byte().to_bytes(1, "big").decode("ascii"), end=" ")
    print()

    m.close()
