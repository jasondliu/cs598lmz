import ctypes

class S(ctypes.Structure):
    x = 1.0

print S().x # should be 1.0
</code>
This doesn't work as I expected. It will give me a segfault:
<code>python test.py
Segmentation fault (core dumped)
</code>
I should be able to work around this by using the <code>_fields_</code> attribute, but I feel like I should be able to do this. Am I doing something wrong or is this not supported?


A:

It works for me on Python 2.7.2 and 3.2.2.
<code>$ python2 test.py 
1.0
$ python2 test.py 
1.0
</code>

