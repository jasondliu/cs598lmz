import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # mmap.error
</code>
Why is this?
This happens on both Windows and Linux with Python 3.3 and 3.4.
Note that this does not happen if the file is opened in "ab" mode (appending only) or if there is more than one byte in the file. This also does not happen if there is more than one byte in the file even if the mode is "r+b" - I guess because the file pointer only gets updated at the end of the file at this point.

