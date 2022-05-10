import io
# Test io.RawIOBase
open('file.tmp','w').close()
f = io.open('file.tmp','r')
f.fileno()

f.name

f.seekable()

# Test that closing a file that was never opened doesn't raise an error
f = io.open('abc')
f.close()

# Test that closing a file that was closed doesn't raise an error
f = io.open('abc')
f.close()
f.close()

# Test file-like object
fio = io.open('file.tmp', 'r')
fio.seek(5)
fio.tell()
fio.flush()
fio.tell()
fio.close()

fio = io.open('file.tmp', 'r')
fio.read()
fio.close()

# Test BufferedReader
f = io.open('file.tmp', 'r')
fb = io.BufferedReader(f)
fb.fileno()

fb.seekable()

fb.name

fb.close()

# Test BufferedWriter

