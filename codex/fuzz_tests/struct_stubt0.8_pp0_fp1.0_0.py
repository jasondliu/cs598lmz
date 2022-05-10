from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'd'
s.size = 8
s.unpack('aaaaa')
</code>
Why do I get this error?


A:

The <code>Struct</code> objects are initialized by the <code>struct</code> module, not by you. If you look at the C code, you'll see that creating the struct object involves some internal struct handling magic.
Also, it is not desirable to mess with the implementation detail of how <code>Struct</code> objects are being constructed.
If you want to create a new <code>Struct</code> object, just call <code>struct.Struct()</code> and pass in your desired format as a parameter.
<code>In [7]: s = struct.Struct('d')
In [8]: s.unpack('aaaaa')
---------------------------------------------------------------------------
error                                     Traceback (most recent call last)

/Users/&lt;ipython-input-8-23d8e3c2c467&gt; in &lt;module&gt;()
----&gt; 1 s.unpack('aaaaa')

/Users/
