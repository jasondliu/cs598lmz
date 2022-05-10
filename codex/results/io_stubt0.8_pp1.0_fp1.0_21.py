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

print("Done.") # from the next line, we see the leaked memory
</code>
If I run this program a few times, I get the following output:
<code>$ python3 leak.py
Done.
$ python3 leak.py
Done.
$ python3 leak.py
Done.
</code>
But if I run this program many times, like this,
<code>$ python3 leak.py &gt;/dev/null &amp;
$ python3 leak.py &gt;/dev/null &amp;
$ python3 leak.py &gt;/dev/null &amp;
$ python3 leak.py &gt;/dev/null &amp;
$ python3 leak.py &gt;/dev/null &amp;
</code>
the memory usage keeps growing and there appears to be no end to it (at least, not within a practical amount of time).
So the question is:
Is there a way I can free the memory allocated by <code>BufferedReader</code> and/or <code>RawIOBase</code> and/or <code>File</code>
