from _struct import Struct
s = Struct.__new__(Struct)
print s
dct = {'format':'3s3sHH','size':Input.size}
s.__dict__.update(dct)
print s
print

print "s._unpack(Input)"
print s._unpack(Input)
print

print "s.unpack_from(Input)"
print s.unpack_from(Input)
print

</code>
The output is:
<code>&lt;_struct.Struct object at 0x7f0bf89678d0&gt;
&lt;_struct.Struct object at 0x7f0bf89678d0&gt;

s._unpack(Input)
('\xf3\xc3\x12', '\x00\x00\x00', 3, 4)

s.unpack_from(Input)
('\xf3\xc3\x12', '\x00\x00\x00', 3, 4)
</code>
I wonder what does <code>size</code> of <code>s</code> mean in the above example? And why does
