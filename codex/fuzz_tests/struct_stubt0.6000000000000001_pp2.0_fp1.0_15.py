from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)
</code>
but I'm getting <code>TypeError: Struct() takes at most 2 positional arguments (3 given)</code>
I know this is not the best way to go but I really need to do it this way.

