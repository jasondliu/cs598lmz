import io
# Test io.RawIOBase
open('file.tmp','w').close()
f = io.open('file.tmp','r')
f.fileno()

f.name

f.seekable()

# Test that closing a file that was never opened doesn't raise an error
