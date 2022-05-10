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
buf = view
print(buf)
print('The code above works on CPython only!')
</code>
In Python 2.7 (and <code>uPy</code>), the code above prints out
<code>'\x00'
The code above works on CPython only!
</code>
While in Python 3.5/3.6 it throws
<code>-----------------------------------------------------------------------
Python 3.5.3+ (default, Feb 27 2017, 18:51:23) 
[GCC 6.3.0 20170221] on linux
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; import io
&gt;&gt;&gt; class File(io.RawIOBase):
...     def readinto(self, buf):
...         global view
...         view = buf
...     def readable(self):
...         return True
... 
&gt;&gt;&gt; f = io.BufferedReader(File())
&gt;&gt;&gt; f.read(1)
----------------------------------------------------------------
