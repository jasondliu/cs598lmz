from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("&gt;I", stream)
print(s.unpack(b'\x00\x00\x00\x00\x00\x00\x00\x00'))
</code>
I know the unpack method has to be called with a byte array of the correct length, but in the python docs it says that the length is the size of the format string.
I can't figure out why I get the following error:
<code>Traceback (most recent call last):
  File "./test.py", line 4, in &lt;module&gt;
    print(s.unpack(b'\x00\x00\x00\x00\x00\x00\x00\x00'))
TypeError: unpack() argument 1 must be string or buffer, not bytes
</code>
I have also tried:
<code>print(s.unpack(b'\x00\x00\x00\x00\x00\x00\x00\x00'.decode('utf-8')))
</code>
Which gets
