from _struct import Struct
s = Struct.__new__(Struct)
s.str = "ciBHiBershB"
s.format = 'ciBHiBershB'
s.size = len(s.str)
</code>
I was also able to reproduce it through the <code>struct.unpack</code> method, but it's much longer to type out!
I was taking a look at the actual C source code for CPython and it clearly allocated more than the few bytes I provided. I haven't done too much digging though. It could be that it's just the cost of garbage collecting the few bytes I gave it. It could also be that I'm doing something that I'm not aware of that is forcing it to allocate much more.


A:

<blockquote>
<p>Python's 'str' is a byte array, so it used to be trivial to allocate structures a byte at a time</p>
</blockquote>
<code>struct.Struct</code> objects will use the buffer interface to pack / unpack data. This is backed by the C API, used by the built-in types. For example, if you create a <code>bytearray</code> instead,
