from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('H')
s.pack()
</code>
Every <code>struct</code> format character has its own <code>__new__</code> and <code>__init__</code> methods that may do whatever makes sense for the given format character.

