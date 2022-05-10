from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('','')
print s.pack(1) # _struct.error: unpack requires a string argument of length 4

class Derived(object):
    def __getattribute__(*args): raise Exception()
d = Derived()
d.x # Segfaults
</code>
Edit: Also, anyone who knows why _struct.error is a string (rather than an exception, or why the string doesn't contain the type of the expected argument?)


A:

<code>_struct.error</code> is an exception class, not an exception instance.  You can catch it in the normal way:
<code>&gt;&gt;&gt; from _struct import Struct
&gt;&gt;&gt; s = Struct.__new__(Struct)
&gt;&gt;&gt; s.__init__('','')
&gt;&gt;&gt; try:
...     s.pack(1)
... except _struct.error as e:
...     print 'caught:', e
... 
caught: unpack requires a string argument
