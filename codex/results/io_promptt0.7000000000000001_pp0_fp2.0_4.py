import io
# Test io.RawIOBase
# Test __init__
print(io.RawIOBase().mode)

f = io.RawIOBase()
buffer = bytearray(b'abcdef')
print(f.readinto(buffer))
print(buffer)

# Test writable
f = io.RawIOBase()
try:
    f.write(b'abc')
except OSError as e:
    print('OSError:', e)

# Test read
f = io.RawIOBase()
try:
    f.read(1)
except OSError as e:
    print('OSError:', e)

# Test readable
f = io.RawIOBase()
print(f.readable())

# Test seekable
f = io.RawIOBase()
print(f.seekable())

# Test read1
f = io.RawIOBase()
try:
    f.read1(1)
except OSError as e:
    print('OSError:', e)

# Test readinto1
f = io.RawIOBase()
try:
