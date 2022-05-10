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
sys.stdout.buffer.write(view)
</code>
I get the result <code>b' '</code>, which is what I want. There's no way to wrap <code>view</code> in <code>memoryview</code> and pass <code>memoryview</code> to <code>write</code> because it doesn't support writing, and the whole point was to achieve putting something into <code>view</code> that could be passed to <code>RawIOBase.write</code> via <code>BufferedWriter.write</code> (and I do need the copy being made, I just assumed it was one of the copies from before).
How would I do this without waiting for it to appear in a future version of Python?

