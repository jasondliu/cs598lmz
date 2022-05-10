from _struct import Struct
s = Struct.__new__(Struct)
file = open('keyfile')
keyfile = file.read()
file.close()
s.pack_into(keyfile)
</code>
However, this returns the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: descriptor 'pack_into' requires a '_struct.Struct' object but received a 'str'
</code>
How can I correctly unpack a struct into a string?


A:

If the structure is the same (which it appears in your case), then the struct module can unpack stuff for you. 
<code>&gt;&gt;&gt; from _struct import Struct
&gt;&gt;&gt; s = Struct('hhl')   # make a new struct object with 2 shorts and 1 long
&gt;&gt;&gt; s.unpack('\x01\x02\x03\x04\x05\x06\x07\x08')   # unpack
(258, 772, 2017
