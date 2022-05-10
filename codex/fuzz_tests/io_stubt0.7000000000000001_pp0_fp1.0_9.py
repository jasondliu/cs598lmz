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
My understanding is that the first time <code>f</code> is deleted, it should call <code>f.__del__</code>, and <code>f.__del__</code> should call <code>f.raw.close</code>, which should call <code>f.raw.__del__</code>, which should call <code>f.raw.flush</code>, which should call <code>f.raw.readinto</code>.
In the first example, it works as expected. In the second, it appears that <code>f.raw</code> is not being garbage collected, so <code>f.raw.__del__</code> is never called.
Why is this? I know that <code>f.raw</code> contains a reference to <code>buf</code> (through <code>view</
