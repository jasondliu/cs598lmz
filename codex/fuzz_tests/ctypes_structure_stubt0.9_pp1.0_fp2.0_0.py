import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ubyte

i = S()
s = '\xc1\x9f'
ctypes.memmove(ctypes.addressof(i), s, len(s))

print i.x
print type(i.x)

</code>
Results:
<code>Python 2.7.15: 
$ python test.py
192
&lt;type 'int'&gt;

Python 3.6.7: 
$ python3 test.py
3327172289
&lt;class 'int'&gt;
</code>
NOTE: If you use <code>ctypes.string_at</code> then you will need to encode your string to accept it in python 2.

