import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print s.x, s.y

s2 = S()
s2.x = 3
s2.y = 4

print s2.x, s2.y

print s.x, s.y
</code>
Output:
<code>1 2
3 4
1 2
</code>
How can I make it so that when I change the value of s2, it also changes the value of s?


A:

You can't.  You can make a new <code>Structure</code> subclass that has a <code>__setattr__</code> method that updates all the other instances of the class:
<code>class S(ctypes.Structure):
    _instances = []
    def __init__(self):
        self._instances.append(self)
    def __setattr__(self, name, value):
        for instance in self._instances:
            setattr(instance,
