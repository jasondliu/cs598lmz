import io
# Test io.RawIOBase
with open("test.txt", "w") as f:
    f.write("Test, test, test\n")
with open("test.txt", "rb") as f:
    raw = io.RawIOBase(f)
    print(raw.readline())

# Test io.BufferedIOBase
with open("test.txt", "w") as f:
    f.write("Test, test, test\n")
with open("test.txt", "rb") as f:
    buff = io.BufferedIOBase(f)
    print(buff.readline())
