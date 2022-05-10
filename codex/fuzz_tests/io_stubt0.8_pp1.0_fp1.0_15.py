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

view.tolist()
[0]
</code>
I believe you can emulate this code using <code>asyncio</code> by using a coroutine that reads into <code>buf</code> and then returns it. This will require two threads and a <code>Queue</code>, but it should work.

