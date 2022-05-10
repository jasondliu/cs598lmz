import io
class File(io.RawIOBase):
    ...
    def fileno(self):
        return super().fileno()

class myfile(File):
    def fileno(self):
        return 42

mf = myfile()
print(mf.fileno())

# The builtin open() function is also a context manager
# It automatically closes the file when the block is exited

with open('/tmp/test.txt', 'r') as f:
    print(f.read())

# Closing a file explicitly closes it and free its resources
f = open('/tmp/test.txt', 'r')
print(f.closed)
f.close()
print(f.closed)

try:
    f.read()
except ValueError as e:
    print(e)

# It's a recommended practice to use the with statement
# as it makes sure the file is closed even in case of an error
# or exception

# If you really want to use the file after it's been closed
# you need to reopen it

f = open('/tmp/test.txt', 'r')
f.close()

