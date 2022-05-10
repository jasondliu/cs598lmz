import mmap
# Test mmap.mmap
with open("data/tinyTale.txt", "r+b") as f:
    mm = mmap.mmap(f.fileno(), 0)
    print("First 10 bytes via read :", mm.read(10))
    print("First 10 bytes via slice:", mm[:10])
    print("2nd 10 bytes via read", mm.read(10))
    mm.seek(0)
    mm.write(b"j" * 10)
    mm.seek(0)
    print("First 10 bytes via read :", mm.read(10))
    print("First 10 bytes via slice:", mm[:10])
    print("2nd 10 bytes via read", mm.read(10))
    mm.close()
    # mm[0] = b"a"
