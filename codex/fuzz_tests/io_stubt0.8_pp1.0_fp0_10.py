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
clib.read_view(view)

# Make sure that a cached entry for File.readinto does not get
# reused for a different type.

class File2(io.RawIOBase):
    def write(self, data):
        pass
f = io.BufferedWriter(File2())
# The next line would crash with a C RuntimeError if the caching
# would be buggy
f.write(b"test")
</code>


A:

I have never had to do it this way.  What I have done is just define the structure as a class.
I have found this to be especially useful when dealing with pointers to a structure because it allows you to use the <code>include</code> property of ctypes (see the docs).  You can do this with a class too, but you must create a new instance of the class each time you get the pointer, when you do it with a structure you can just instantiate the structure once and pass the same instance to all functions that return pointers to the structure.
The structure is defined as a class.  It has all the data members defined as class members.  Here is a
