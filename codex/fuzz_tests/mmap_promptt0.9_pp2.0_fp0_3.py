import mmap
# Test mmap.mmap()
# Response:
#   &lt;class 'mmap.mmap'&gt;
#   bytearray(b'foo foo')
#   &lt;class 'bytearray'&gt;
#   b'foo'
#   &lt;class 'bytes'&gt;
#   b'foo foo'
</code>
Test2:
test2.py
In this example, I try to use <code>mmap.mmap()</code> in a more complex program.  I get the same result as the code example I give in the answer.
<code>#!/usr/bin/python3.7
# test2.py

import os
import mmap
import sys

print(os.getcwd())
print(sys.executable)
file_to_map = open("./foo.txt","r+")
file_memory_object = mmap.mmap(file_to_map.fileno(),0)
print(type(file_memory_object))
file_content = file_memory_object.read()
print(file_
