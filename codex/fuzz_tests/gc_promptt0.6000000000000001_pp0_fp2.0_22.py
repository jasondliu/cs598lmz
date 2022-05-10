import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
# Create some objects
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)
a = A(10)
b = A(20)
c = A(30)
d = A(40)
e = A(50)
f = A(60)
a1 = A(70)
a2 = A(80)
a3 = A(90)
# Create a cycle involving a and b
a.other = b
b.other = a
# Create a cycle involving c and d
c.other = d
d.other = c
# Create a cycle involving e and f
e.other = f
f.other = e
# Create a cycle involving a1 and a2
a1.other = a2
a2.other = a1
# Create a cycle involving a2 and a3
a2.other2 = a3
a3.other2 = a2
# Break the cycle involving a and b
a.other = None
b.
