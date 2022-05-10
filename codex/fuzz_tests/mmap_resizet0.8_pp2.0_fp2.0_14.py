import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
And I get the exception: <code>ValueError: cannot mmap an empty file</code>
It's strange of course, but why I get an exception when <code>m</code> is not empty? I have this problem because in my code I have <code>mmap</code> object and when I'm doing some other stuff, the file get empty and my <code>mmap</code> raises an exception.
One way to avoid this situation is to store the state of mmap before doing some other stuff and restore it afterwards. But is it possible to avoid that?
UPD: The code of my class was a bit more complex so I've added some <code>import</code>s and more code:
<code>import os
import mmap

class Test(object):
    def __init__(self):
        self.f = open('test', 'wb')
        self.f.write(bytes(1))
        self.f.flush()

        self.m = mmap.mmap(self.f.fileno(), 0)

    def do_stuff(self):
