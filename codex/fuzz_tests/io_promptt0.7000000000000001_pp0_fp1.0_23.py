import io
# Test io.RawIOBase.readall()

# Create a file object and write a few lines to it
# fileobj = io.StringIO()
fileobj = io.BytesIO()
fileobj.write(b'Hello!\n')
fileobj.write(b'Second line\n')
fileobj.write(b'Third line\n')

# Read in the entire file
fileobj.seek(0)
data = fileobj.readall()

# Print out the data that was read in
print('File contents: {!r}'.format(data))
# File contents: b'Hello!\nSecond line\nThird line\n'
