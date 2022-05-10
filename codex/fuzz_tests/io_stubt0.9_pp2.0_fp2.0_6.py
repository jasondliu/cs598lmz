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
view
(Casting to an array is a customization point for bytearray.)
</code>
Note: I'm only showing here how to read, but you can write in a similar way. Further note: The <code>io</code> module is really complex and you can even subclass from <code>RawIOBase</code> if you don't want to cast your buffers to memory views. But for the purposes of your question, this is a good workaround.

