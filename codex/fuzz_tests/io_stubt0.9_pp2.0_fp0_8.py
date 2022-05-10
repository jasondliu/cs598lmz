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
sys.getrefcount(view)
</code>
Edit 3:
If I create a BufferedRandom instead of a BufferedReader, The only way I can make readinto work is to return the wrong amount of data.
Code:
<code>class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
        return 4
    def readable(self):
        return True

f = io.BufferedRandom(File())
f.read(1)
del f
sys.getrefcount(view)
</code>
Conclusion
The only way I could get the file reader's readinto() method to work was by returning the wrong number.  If I return the correct value of the amount of data placed into the buffer, the data is not written to the buffer.  and so read() does not get the data, and it is garbage collected.
It seems to me the bug is on the BufferedReader's side.  It is trying to enforce a restriction on data to be placed into the buffer, based on the amount of data the user requested, not the amount actually placed into the buffer
