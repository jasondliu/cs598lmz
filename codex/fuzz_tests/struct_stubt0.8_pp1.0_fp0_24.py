from _struct import Struct
s = Struct.__new__(Struct)
s.__init__(s, 'hi')
s.pack(1,2)
</code>
As expected, this code works fine.
Now, if we change the <code>type(s)</code> to <code>type(Struct)</code>, it doesn't work anymore:
<code>from _struct import Struct
Struct.__new__(Struct)
s = type(Struct)()
s.__init__(s, 'hi')
s.pack(1,2)
</code>
The error is as follows:
<code>---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
&lt;ipython-input-39-00ad41c61db1&gt; in &lt;module&gt;()
      1 from _struct import Struct
      2 Struct.__new__(Struct)
----&gt; 3 s = type(Struct)()
      4 s.__init__(s, 'hi')
      5 s.pack(1,2)

TypeError: Required argument 'format' (pos 1) not found
</code>
I don't quite
