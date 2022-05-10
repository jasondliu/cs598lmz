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
gc.collect()
print(view)
</code>
This will print <code>None</code> if the object is collected, and in my tests, it is collected in both CPython and PyPy. As for whether it is guaranteed to be collected, it depends on how CPython is implemented. It could be that the GC tries to keep objects in the nursery for as long as possible, so you might have to do <code>del view</code> after reading from the file, but I don't think that is the case.
If you are worried about this object being collected, you could always use a <code>bytearray</code> instead. <code>bytearray</code>s are mutable and they will always be freed immediately after you no longer have a reference to them:
<code>view = bytearray(1)
</code>

