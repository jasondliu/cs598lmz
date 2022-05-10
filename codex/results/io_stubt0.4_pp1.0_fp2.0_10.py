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
When I run it, I get the following error:
<code>Exception ignored in: &lt;bound method BufferedReader.__del__ of &lt;_io.BufferedReader name=&lt;__main__.File object at 0x7f9f9d9e9a00&gt;&gt;&gt;
Traceback (most recent call last):
  File "/usr/lib/python3.6/io.py", line 613, in __del__
  File "/usr/lib/python3.6/io.py", line 571, in close
  File "/usr/lib/python3.6/io.py", line 860, in detach
ValueError: underlying buffer has been detached
</code>
I don't understand what's going on. I thought the <code>BufferedReader</code> would keep the <code>File</code> object alive, but it doesn't. Is there a way to make it work?


A:

The problem is that the <code>io.BufferedReader</code> keeps a reference to the <code>io.
