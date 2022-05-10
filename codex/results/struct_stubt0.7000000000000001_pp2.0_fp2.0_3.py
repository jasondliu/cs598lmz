from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4
a = s.pack(1)
s.size = 8
s.pack(2)
</code>
Output: 
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python2.7/struct.py", line 483, in pack
    "wrong size for " + self.__name__)
error: size changed, cannot pack
</code>

