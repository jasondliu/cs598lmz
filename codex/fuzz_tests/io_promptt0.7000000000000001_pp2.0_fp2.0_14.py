import io
# Test io.RawIOBase.readinto
# Test io.RawIOBase.readinto1

import io
import os

# Create a file and get its size
f = open(os.path.join(os.path.dirname(__file__), 'readinto.dat'), 'wb')
f.write(os.urandom(100))
f.close()
st = os.stat(f.name)

# Test reading the entire file
f = open(f.name, 'rb')
buf = bytearray(st.st_size)
assert f.readinto(buf) == st.st_size
assert buf == f.read()
f.close()

# Test reading part of the file
f = open(f.name, 'rb')
buf = bytearray(20)
assert f.readinto(buf) == 20
assert buf == f.read(20)
f.close()

# Test reading the entire file using readinto1
f = open(f.name, 'rb')
buf = bytearray(st.st_size)
while f.readinto1
