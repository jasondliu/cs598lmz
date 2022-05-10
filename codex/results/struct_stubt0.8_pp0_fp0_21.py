from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('bbBHIh')
# TypeError: 'Struct' object is not callable
</code>
Expected:
<code>&gt;&gt;&gt; Struct('bbBHIh').pack(1, 1, 1, 1, 1, 1)
b'\x01\x01\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01'
</code>


A:

There is a good reason why <code>Struct</code> is not callable -- it is an abstract base class for other struct classes, that define the exact size and layout of the struct.
You can see from the documentation:
<blockquote>
<p>Changed in version 3.3: Struct is now an abstract type (ABC).</p>
</blockquote>
and
<blockquote>
<p>Abstract base class for the struct (binary data) module.</p
