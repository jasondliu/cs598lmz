import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read(1))
</code>
The problem I'm having is that I want to use <code>mmap.mmap()</code> with a file opened on an <code>http.client.HTTPResponse</code> object, and the documentation for <code>mmap.mmap()</code> specifically says that it is not supported with <code>mmap.ACCESS_READ</code>. 
Here's a related question: mmap on large text file without loading in memory python
In this question, "read" is used in a Python sense, in the sense of <code>file.read()</code>. Because <code>http.client.HTTPResponse</code> files are iterators, they can't be read in this sense, which is why <code>mmap</code> is failing.
The same problem prevents me from being able to do <code>seek</code>s on these response objects. It seems that at some point these http response objects must be downloaded to memory, as I am able to do an <code>iter</code> on them and get the line count that way (<
