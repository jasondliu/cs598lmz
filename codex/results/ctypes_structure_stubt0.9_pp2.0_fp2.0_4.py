import ctypes

class S(ctypes.Structure):
    x = 16*ctypes.c_double()

s = S()

for i in range(0,16):
    s.x[i] = i

print s

for i in range(0,16):
    print "%d = %f" % (i, s.x[i])
</code>
But here, the output of s.x[i] is increasing by 8 when i increase only by 1. Is this a bug from ctypes ? How can I access to the values of the allocated array ? 
I know that the array will have 16 * 8 * 8 bytes (the same size as the pointer - so no space to store the values) but I still don't understand why the value is at 8 * i.
The output I have with python 2.7 is :
<code> $ python s.py 
    ./s.py:10: DeprecationWarning: inserting an item that is not an integer into x will result in an error in the future
  s.x[i] = i
&lt;__main__.S instance at 0xb7676aec&gt;
0 = 0.000000

