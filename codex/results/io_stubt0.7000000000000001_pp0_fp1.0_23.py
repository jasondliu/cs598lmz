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
I have a global <code>view</code> that I can get by importing the module.
But I cannot delete the object. 
<code>&gt;&gt;&gt; del f
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
NameError: name 'f' is not defined
&gt;&gt;&gt; f
&lt;io.BufferedReader name=''&gt;
</code>
Why does it have a name? How can I find out what is holding the reference?
I am using Python 3.6.2.


A:

Per the docs, <code>BufferedReader</code> is a "context manager". It is automatically closed when the <code>with</code> block ends.
So, you can assign the object, but it only lives for the duration of the block.
<code>with io.BufferedReader(File()) as f:
    f.read(1)
    del f
print(f)
</code>
This prints
