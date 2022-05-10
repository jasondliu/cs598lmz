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

f = io.BufferedReader(File())
f.read(1)
del f

f = io.BufferedReader(File())
f.read(1)
del f

#io.BufferedReader accesses the buffer directly if it sees a known object.
#It doesn't check for the object's actual type. If a new object with the
#same identity is created, then io.BufferedReader's readinto function would
#fail.

#output:
#fatal error: fatal error: BufferError: buffer is too small for requested bytes

#This doesn't mean that you should use a repr() to test for equality, though.
#If you're using a type that can be subclassed with a  __eq__  operator, then
#the subclass could override it to do something other than memory comparison.

#If you need to perform a type and value check, use the  isinstance  function
#to do so.

#IOErrorIf you want to access a file or socket, it's much more efficient to
#wrap it in a buffered object than to access it directly.

#If
