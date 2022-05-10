import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

x = S()
y = S()

x.x, x.y = 1, 2
y.x, y.y = 3, 4

print 'x', x.x, x.y      # 1, 2
print 'y', y.x, y.y      # 3, 4

x = y
y.x = 5

print 'x', x.x, x.y      # 5, 4
print 'y', y.x, y.y      # 5, 4
</code>
My question is why the last two lines show <code>x 5 4</code> and <code>y 5 4</code>?
At the end, <code>y.x = 5</code> should only modify <code>y</code> not <code>x</code>. I'm confused.


A:

In python assignments never copy, they just create a new reference to the same object. Even if you are using types from the <code>ctypes</code> module.
You can see this from your
