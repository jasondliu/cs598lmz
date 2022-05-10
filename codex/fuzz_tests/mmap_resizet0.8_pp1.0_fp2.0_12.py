import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]       # this fails
                                                                                    --
                                                                                    1
                                                                                    2
                                                                                    3
                                                                                    4
                                                                                    5
                                                                                    6
                                                                                    7
                                                                                    8
                                                                                    9
                                                                                    10
                                                                                    11
                                                                                    12
                                                                                    13
</code>


A:

As per the documentation for the <code>mmap</code> module in the standard library, it will not be updated if the file is truncated. 
<blockquote>
<p>Note that modifications to the mmap object are not written through
  to the file unless flush() or close() is called.</p>
</blockquote>
You need to close the file handle, truncate it and open it again.

