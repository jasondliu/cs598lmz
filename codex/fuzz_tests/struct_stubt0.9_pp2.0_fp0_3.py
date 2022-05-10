from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('b', (1,))
buf = s.pack(42)
s2 = Struct.__new__(Struct)
s2.__init__('b', (1,))
</code>
One can guess what's going on. <code>__init__</code> is creating a new struct, and that struct is getting collected. <code>__new__</code> can be considered similar to Java's <code>new</code>, where you can create the object, but it is not usable until it is initialized. In other words, the <code>struct</code> object needs to be constructed and initialized before it can be used.
So, they do different things. Python knows how to construct an object. It doesn't know how to initialize it (it knows how to call <code>__init__</code> if that method is defined, but it can't know how to construct the object without it). You'd run into the same situation if you had a class that accepted this kind of initialization:
<code>class Point(object):
  def __init__(self, x, y):
    self.x = x

