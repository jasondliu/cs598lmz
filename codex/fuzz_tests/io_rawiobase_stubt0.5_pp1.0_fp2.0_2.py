import io
class File(io.RawIOBase):
    def write(self, b):
        print(b)
        return len(b)

f = File()
f.write(b'hello')

# File.write() is a method, so it has a self parameter.
# RawIOBase.write() is a function, so it does not.

# The self parameter is automatically set to the object that is accessing the method.
# This is the same way that the self parameter works in class methods.

# The self parameter is not just a convention.
# The Python interpreter uses the self parameter to determine which object is accessing the method.

# In the above example, the File class inherits from RawIOBase.
# The File class also overrides the write() method.
# When you call f.write(b'hello'), Python automatically sets the self parameter to f.
# The self parameter is a way for Python to keep track of which object is accessing the method.

# If you call RawIOBase.write() directly, you need to provide the self parameter.

# Example
# Call the write() method directly on the RawIOBase class.
RawIOBase.
