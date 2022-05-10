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

print(view)

# A buffer is not deallocated if it is still referenced by the object
# that allocated it.

# This is the case for a file object's internal buffer.

# However, the buffer is deallocated when the file object is deleted.

# This is a problem if the buffer is used by a different object.

# The buffer is deallocated, and the other object is left with a dangling
# pointer.

# This is the case for io.BufferedReader.

# The buffer is used by the file object.

# The buffer is deallocated when the file object is deleted.

# The buffer is used by the BufferedReader.

# The buffer is deallocated when the file object is deleted.

# The buffer is used by the global variable view.

# The buffer is deallocated when the file object is deleted.

# The global variable view is left with a dangling pointer.

# This is a problem for the Python garbage collector.

# The garbage collector does not know that the buffer is deallocated.

# The garbage collector thinks that
