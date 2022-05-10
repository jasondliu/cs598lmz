from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\x5d\x00\x00\x80\x0e\xff\xff\xff\xff')

# We'll be learning more about the "with" keyword in this lesson,
# but I'm including it here since it's necessary for a few of the
# examples below.
#
# When we're using the "with" keyword, we don't need to call the
# close() method on our file handle.
#
# It lets Python handle it automatically.
with open('example.txt', 'w') as f:
    f.write('example file')

# If you want to immediately know the process id (in the Unix
# world), you can use the getpid() method.
import os
os.getpid()

# Sometimes you want to check if a process is still running.  The
# getppid() method will give you the parent's process id.
os.getppid()

# You can get the current user id and group id with the getuid()
# and getgid() methods.
os.getuid()
os.getgid()
