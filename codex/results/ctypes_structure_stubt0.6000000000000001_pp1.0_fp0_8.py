import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char
    y = ctypes.c_char

s = S()

s.x = 'a'
s.y = 'b'
print s.x
print s.y

print s.__dict__

print '\n'

class C(object):
    def __init__(self):
        self.x = 'a'
        self.y = 'b'

c = C()

print c.x
print c.y
print c.__dict__
</code>
The output is :
<code>a
b
{}

a
b
{'y': 'b', 'x': 'a'}
</code>
So the question is: why <code>S</code> does not have any attribute?


A:

The <code>__dict__</code> attribute is not a special property of the <code>ctypes.Structure</code> class. It's just a normal attribute, which is not set by default. You can set it yourself:
<code>class S(ctypes.Structure):
