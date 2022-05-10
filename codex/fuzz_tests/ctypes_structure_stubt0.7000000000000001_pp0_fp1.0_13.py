import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

a = S()
a.x = 1
a.y = 2

b = S()
b.x = 3
b.y = 4

c = S()
c.x = 5
c.y = 6

# This works
a = b = c = S()
</code>
I want to do the same thing in python, but the above does not work.
<code>class S:
    def __init__(self):
        self.x = 0
        self.y = 0

a = S()
a.x = 1
a.y = 2

b = S()
b.x = 3
b.y = 4

c = S()
c.x = 5
c.y = 6

# This does not work
a = b = c = S()
</code>
I understand that in python, assignment statements evaluate from right to left, so the above code really means <code>a = b; a = c; a = S();</code>. But is there a way to
