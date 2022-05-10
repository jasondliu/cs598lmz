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
del view
</code>
The garbage collector triggers the finalizer of <code>BufferedReader</code>, which then tries to read the underlying file, but fails because it has been garbage collected already.
This is a separate issue from the crash. There is already a bug report, and a patch has been submitted.

