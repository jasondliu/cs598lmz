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

print(io.StringIO().read(1))
</code>
The output of the script is:
<code>b'\xb3'

Traceback (most recent call last):
  File "test.py", line 15, in &lt;module&gt;
    print(io.StringIO().read(1))
TypeError: string argument expected, got 'int'
</code>
It looks like the <code>io.TextIOWrapper</code> object created by the <code>StringIO</code> constructor expects and integer as its <code>buffer</code> argument instead of a <code>BufferedReader</code>.
Am I doing something wrong or is this a bug?

