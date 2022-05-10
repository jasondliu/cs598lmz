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
It prints <code>None</code>, which is not what I expected.
I know that I can use <code>weakref.proxy</code> to make a proxy object that doesn't keep the object alive, but I would like to know why the above code doesn't work.


A:

<blockquote>
<p>I know that I can use <code>&lt;code&gt;weakref.proxy&lt;/code&gt;</code> to make a proxy object that doesn't keep the object alive, but I would like to know why the above code doesn't work.</p>
</blockquote>
The code does work, but not in the way you expect. 
The <code>io.BufferedReader</code> instance keeps a reference to the <code>File</code> instance, and the <code>io.BufferedReader</code> instance is kept alive by the <code>f</code> reference.
The <code>io.BufferedReader</code> instance keeps a reference to the <code>view</code> object, but that reference is not kept alive
