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
print(view)
</code>
The above code will print <code>b''</code> on Python 3.4.3 but <code>b'\x00'</code> on Python 3.5.1.
This is a problem for me because I'm working on a library that depends on the Python 3.4.3 behaviour.
My question: is this a bug in Python 3.5.1 or is it a change to the language that I need to work around? If it's the latter, what is the correct way to work around it?


A:

The Python 3.5.1 behaviour is correct.
<blockquote>
<p>The <code>&lt;code&gt;readinto()&lt;/code&gt;</code> method is intended to allow efficient reading of data into an existing buffer. The <code>&lt;code&gt;readable()&lt;/code&gt;</code> method should be overridden to indicate whether the object supports <code>&lt;code&gt;readinto()&lt;/code&gt;</code>.</p>
