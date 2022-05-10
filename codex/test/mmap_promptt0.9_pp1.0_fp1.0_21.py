import mmap
# Test mmap.mmap( )
f = open('script.py')
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
print(m[:60])

print()

# Thanks a lot to python mmap
string = 'hello world'
m = mmap.mmap(-1, len(string)) # mmap 0 byte length
# TypeError: mmap length is positive
m.write(string.encode())
print(m[:])

m.seek(0) # move to the beginning of the mmap
print(m.read(len(string)))

m.close()

print()

# BytesIO test 
# writable, readable, seekable
print('Create BytesIO : ')
s = io.BytesIO()
print(s.write(b'Hello World'))
# return int , this is number of bytes written
print('Read by getvalue() : ')
print(s.getvalue())

print()

# Couldn't write and seek by it
