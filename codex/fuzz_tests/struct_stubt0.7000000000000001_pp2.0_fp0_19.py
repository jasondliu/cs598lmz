from _struct import Struct
s = Struct.__new__(Struct)

s.size = lambda: 5

# TypeError: 'Struct' object is not callable
s.pack(1)
</code>

Why is <code>Struct</code> not callable?
Why do I get <code>TypeError</code> even though <code>Struct</code> has <code>pack</code> method?
Why does <code>Struct</code> have <code>pack</code> method?

Is there any way I can bypass these issues to achieve my goal?

