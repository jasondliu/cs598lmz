import io
# Test io.RawIOBase.

# .readall()
print(io.RawIOBase.readall.__doc__)
with open("sample.txt", "rb") as f:
    print(f.readall())

# .readinto()
print(io.RawIOBase.readinto.__doc__)
with open("sample.txt", "rb") as f:
    b = bytearray(10)
    n = f.readinto(b)
    print(n)
    print(b)

# .readinto1()
print(io.RawIOBase.readinto1.__doc__)
with open("sample.txt", "rb") as f:
    b = bytearray(10)
    n = f.readinto1(b)
    print(n)
    print(b)

# .read()
print(io.RawIOBase.read.__doc__)
with open("sample.txt", "rb") as f:
    print(f.read(10))

# .read1()
print(io.RawIOBase.read1
