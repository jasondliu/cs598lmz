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
Next, if you do care about such things (i.e. you are a responsible programmer), then you must use capabilites to ensure your container cannot access <code>f</code>. This is done by declaring a capability <code>name=""; export name;</code> in your <code>runc</code> JSON configuration file to remove the names that are in the default namespace.

