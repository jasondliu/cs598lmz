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
Output:
<code>b'\x00'
</code>
However, when doing the same thing with <code>io.BytesIO</code>, an error is raised:
<code>import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BytesIO(File())
f.read(1)
del f
print(view)
</code>
Output:
<code>Traceback (most recent call last):
  File "test.py", line 12, in &lt;module&gt;
    print(view)
UnboundLocalError: local variable 'view' referenced before assignment
</code>
Apparently, the <code>view</code> object is no longer available once <code>f</code> is deleted. But why?


A:

I think the issue is that <code>__exit__</code> of <code>BytesIO</code> is calling <code>close</code>
