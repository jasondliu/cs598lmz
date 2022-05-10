from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('4s')
s.pack('aaaa')
s.pack('bbbb')
s.pack('cccc')
s.pack('dddd')
s.pack('eeee')
</code>
I want the output to be 'aaaa' 'bbbb' 'cccc' 'dddd' 'eeee'. But the output is 'aaaa' 'aaaa' 'aaaa' 'aaaa' 'aaaa'.
Why is this happening?


A:

You have to create a new <code>Struct</code> object for each call to <code>pack</code>.
<code>from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('4s')
s.pack('aaaa')
s.pack('bbbb')
s.pack('cccc')
s.pack('dddd')
s.pack('eeee')
</code>
creates one struct object <code>s</code>.
<code>from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('4s')
s.pack('aaaa')
