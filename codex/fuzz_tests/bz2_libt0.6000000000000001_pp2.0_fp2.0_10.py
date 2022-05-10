import bz2
bz2.open("../data/test.xml.bz2")
</code>
this works well.
But when I do
<code>from bz2 import open as bzopen
bzopen("../data/test.xml.bz2")
</code>
I get
<code>AttributeError: 'module' object has no attribute 'open'
</code>
and when I do
<code>from bz2 import open
open("../data/test.xml.bz2")
</code>
I get
<code>IOError: [Errno 2] No such file or directory: '../data/test.xml.bz2'
</code>
What is going on?


A:

The <code>open()</code> function in the <code>bz2</code> module is not a function that returns a file object for a file in the filesystem. It's a function that creates a new file object for a file-like object that supports bzip2 compression.
Your <code>from bz2 import open</code> statement is actually importing <code>bz2.
