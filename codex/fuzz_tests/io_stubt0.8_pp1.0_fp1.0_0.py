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
print view[0]
</code>
That said, I am completely unable to find the code inside Python 3.1.1 that does the global lookup for the <code>view</code> variable (maybe I just don't know where to look).
Edit: The code that I believe is responsible for this behavior can be found in the source of Python 3.1.1 at <code>Python/ceval.c:378</code>. My C skills are rather rusty, but it appears to me that the <code>LOAD_GLOBAL</code> opcode is replaced on the stack with the value of the <code>view</code> variable (see <code>Python/ceval.c:379</code> and <code>Python/ceval.c:366</code>).
What I still don't understand is why this does not happen for reading from a file. I suspect that some additional check is performed for builtin types.


A:

I think this is a bug:
<code>$ python3.1 -c 'from io import BytesIO; f = BytesIO(b"a"); f.read(1); del f
