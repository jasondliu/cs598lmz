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
print(view)
</code>
The "obvious" solution would be to add a <code>__del__</code> to <code>io.BufferedReader</code>, but I'd rather avoid patching the stdlib.
Is there a way to do this without patching the stdlib?

