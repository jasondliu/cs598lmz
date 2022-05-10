import io
# Test io.RawIOBase.readall

# Try to readall on a normal file, should just read the entire contents.
print('TEST 1:')
f = io.BytesIO(b'abc\x00d\xe5\xf6\x00ghi\x00j')
print(f.readall())

# Try to readall on a file that claims to be too big for the address
# space.  Should raise OverflowError (or MemoryError on 32-bit systems)
f = io.BytesIO(b'x' * (10 * 1024 * 1024))
print('TEST 2:')
try:
    f.readall(8 * 1024 * 1024)
except (OverflowError, MemoryError):
    print('OK')
else:
    print('READALL() DID NOT RAISE')

# Try to readall on a file that claims to be too big for the address
# space, but is in fact much smaller.  Should read all of the data.
print('TEST 3:')
f = io.BytesIO(b'x' * (10 * 1024 * 1024))
print(len(f
