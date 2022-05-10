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
</code>
As you can see, the idea is to give <code>readinto</code> an out-variable that's globally available. You can then read from it as a global variable, and even write to it, if that helps.
But, as I said above, it's not very elegant, so I would only use it if I didn't have a better way.

