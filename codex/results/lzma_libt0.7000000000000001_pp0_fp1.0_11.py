import lzma
lzma.open(filename)
</code>
I'm getting the following error:
<code>AttributeError: 'module' object has no attribute 'open'
</code>
I've tried to look for an answer and apparently it's because I'm running python 2.6.
I've tried to install pylzma but when I try to import pylzma I'm getting the same error. 
How can I open lzma files with Python 2.6?


A:

<code>import lzma
with lzma.open(filename, mode='rt') as f:
    content = f.read()
</code>
Python 2.6 only has <code>lzma.open</code> in a hacky form which only supports reading.

