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
</code>
But, of course, this doesn't work. The <code>readinto</code> method writes into <code>buf</code>, but does not update the current position in the buffered reader. So the <code>read</code> method reads into its internal buffer, and then returns the whole string before <code>view</code> got its chance to dump the internal buffer's contents.
Is there any other, easier way (using <code>io</code> functionality) to achieve the same effect? Of course, I'd prefer not to have to reimplement all the buffering logic myself.


A:

Since no one else had an answer, I'm posting my own solution. I implemented a subclass of <code>io.BufferedReader</code> that inherits all of its functionality, and then overrides the <code>readinto</code> method to dump into the given buffer instead of the underlying one. Also, if the internal buffer is empty, then <code>readinto</code> calls the <code>readinto</code> method of the underlying buffer, since there's now no buffered data to write into the user
